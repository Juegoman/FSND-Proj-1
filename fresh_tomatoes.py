import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My favorite Animes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .anime-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .anime-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .flex {
            display: flex;
            flex-direction: row;
            min-width: 100px;
            flex-wrap: wrap;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal',
        function (event) {
            // Remove the src so the player itself gets removed,
            // as this is the only reliable way to ensure the video stops
            // playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.anime-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId
            + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>",
            { 'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        //On hovering over a tile, the description is shown.
        $(document).on('mouseenter mouseleave', '.anime-tile', function (e) {
            $(this).find('p').toggleClass("hidden");
        });
        // Animate in the animes when the page loads
        $(document).ready(function () {
          $('.anime-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal"
            aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Anime Library</a>
          </div>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="https://github.com/juegoman" target="_blank">made by @juegoman</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container flex">
      {anime_tiles}
    </div>
  </body>
</html>
'''


# A single anime entry html template
anime_tile_content = '''
<div class="col-md-6 col-lg-4 anime-tile text-center"
    data-trailer-youtube-id="{op_youtube_id}" data-toggle="modal"
    data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{anime_title}</h2>
    <p class="hidden">{anime_synopsis}</p>
</div>
'''


def create_anime_tiles_content(animes):
    # The HTML content for this section of the page
    content = ''
    for anime in animes:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', anime.op_yt_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', anime.op_yt_url)
        op_yt_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the anime with its content filled in
        content += anime_tile_content.format(
            anime_title=anime.title,
            poster_image_url=anime.image_url,
            op_youtube_id=op_yt_id,
            anime_synopsis=anime.synopsis
        )
    return content


def open_animes_page(animes):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the anime tiles placeholder generated content
    rendered_content = main_page_content.format(
        anime_tiles=create_anime_tiles_content(animes))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
