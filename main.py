import media
import fresh_tomatoes

#Instantiate the catalog of animes

one_punch_man = media.Anime("One Punch Man", "A bald man with godlike strength"
                   " defeats everything with one punch.",
                   "http://1.bp.blogspot.com/-jwEBw38AdYg/VpWvlPePs_I/AAAAAAAABcc/K4Z11tWG0S8/s1600/One-Punch%2BMan.jpg",# NOQA
                   "https://www.youtube.com/watch?v=atxYe-nOa9w")

kill_la_kill = media.Anime("Kill la Kill", "Ryuuko Matoi goes to Honnouji "
                   "Academy to find the truth about her father's death.",
                   "http://67.media.tumblr.com/e2f980674e38f32a5e17b428a5e07005/tumblr_nye3k9orf61rc1nzgo5_1280.jpg",# NOQA
                   "https://www.youtube.com/watch?v=scRQ3AXe4hw")

symphogear = media.Anime("Senki Zesshou Symphogear", "After recovering from a "
                   "near fatal injury in a mysterious attack, Hibiki Tachibana "
                   "must use her new powers to defeat malevolent forces.",
                   "http://3.bp.blogspot.com/-9mQP3GV1fts/VZDW93qzfgI/AAAAAAAAAwU/vro2XpGu9ew/s1600/%25E6%2588%25B0%25E5%25A7%25AC%25E7%25B5%2595%25E5%2594%25B1.jpg",# NOQA
                   "https://www.youtube.com/watch?v=FOXaWCRv_68")

katanagatari = media.Anime("Katanagatari", "A mysterious woman seeks out a "
                   "hermit with knowledge of a lost martial art to collect "
                   "cursed blades.",
                   "http://media.senscritique.com/media/000006512004/source_big/Katanagatari.jpg",# NOQA
                   "https://www.youtube.com/watch?v=Bs4VBfpIaes")

jojo = media.Anime("JoJo's Bizarre Adventure", "The Joestar bloodline wages a "
                   "never ending battle against various supernatural forces.",
                   "http://i.imgur.com/d2cHMKb.jpg",
                   "https://www.youtube.com/watch?v=8ZtGDSZie5I")

gurren_lagann = media.Anime("Tengen Toppa Gurren Lagann", "Simon and his "
                   "brother Kamina live in squalor underground when their home "
                   "is attacked and they are forced to embark on an adventure "
                   "to free humanity." ,
                   "http://static1.squarespace.com/static/520a5868e4b01247d70eaa07/54f9ea91e4b0bde11db053ac/54fc0403e4b0da385be147ab/1425802255985/Gurren+Lagann.jpg",# NOQA
                   "https://www.youtube.com/watch?v=C_t47BVtPuE")

#Add the instantiated animes to a list

animes = [one_punch_man, kill_la_kill, symphogear,
          katanagatari, jojo, gurren_lagann]

#send the list to the fresh_tomatoes module for rendering
fresh_tomatoes.open_animes_page(animes)
