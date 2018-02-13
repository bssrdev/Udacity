import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pele = media.Movie("Pele",
                   "Birth of a Legend",
                   "https://upload.wikimedia.org/wikipedia/en/d/df/"
                   "Pel%C3%A9_%28film_poster%29.jpg",
                   "https://www.youtube.com/watch?v=pwBXs2B2ZbI")

blackpanther = media.Movie("Blackpanther",
                           "Vokanda",
                           "https://upload.wikimedia.org/wikipedia/en/0/0c/"
                           "Black_Panther_film_poster.jpg",
                           "https://youtu.be/xjDjIWPwcPU")

ironman = media.Movie("Ironman",
                      "The Man behind the Iron Suit",
                      "https://upload.wikimedia.org/wikipedia/en/7/70/"
                      "Ironmanposter.JPG",
                      "https://youtu.be/8hYlB38asDY")

thorragnarock = media.Movie("Thor Ragnarock",
                            "The Legend of Thunder",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/"
                            "Thor_Ragnarok_poster.jpg",
                            "https://youtu.be/ue80QwXMRHg")


movies = [toy_story, avatar, pele, blackpanther, ironman, thorragnarock]
fresh_tomatoes.open_movies_page(movies)
