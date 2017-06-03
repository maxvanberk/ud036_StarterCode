import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to live",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
                       "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://goo.gl/images/0pyHPM",
                     "https://youtu.be/5PSNL1qE6VY")


fight_club = media.Movie("Fight Club",
                        "Man's chronic insomnia gets out of hand",
                         "https://goo.gl/images/YtrL8W",
                         "https://youtu.be/SUXWAEX2jlg")

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
      
movies=[toy_story,avatar,fight_club]

fresh_tomatoes.open_movies_page(movies)

                        

                       
