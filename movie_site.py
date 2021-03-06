import media
import fresh_tomatoes

# Here we create instances of the class Movie.
# They can be used to build the movie site further down the road

shining = media.Movie("The Shining",
                    "Man get's a bad case of "
                    "cabin fever but finally chills",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcSO0FTIrcYQ_r6QDHclHKOKBHMY9FlUENGVRUYpcHCEGRUaHupG",  # noqa
                    "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

matrix = media.Movie("The Matrix",
                    "Batteries go bad",
                    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

full_mtl_jacket = media.Movie("Full Metal Jacket",
                    "Hilarious drill sergeant trolls a dip-shit"
                    " ...then it turns out that war is unpleasant",
                    "https://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",  # noqa
                    "https://youtu.be/x9f6JaaX7Wg")

twelve_monkeys = media.Movie("Twelve Monkeys",
                    "People from the future repeatedly bend Bruce Willis "
                    "back in time to save the world. He fails",
                    "https://upload.wikimedia.org/wikipedia/en/c/cf/Twelve_monkeysmp.jpg",  # noqa
                    "https://youtu.be/15s4Y9ffW_o")

alien = media.Movie("Alien",
                    "Crew of commercial deep space vessel learns the hard "
                    "way why medical safety protocols exist",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BNDNhN2IxZWItNGEwYS00ZDNhLThiM2UtODU3NWJlZjBkYjQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,681,1000_AL_.jpg",  # noqa
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")


fight_club = media.Movie("Fight Club",
                    "Man's chronic insomnia gets out of hand",
                    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",  # noqa
                    "https://youtu.be/SUXWAEX2jlg")

# create a list of movies to show on the movie site
movies = [shining, matrix, full_mtl_jacket, twelve_monkeys, alien, fight_club]

# Create the movies page
fresh_tomatoes.open_movies_page(movies)
