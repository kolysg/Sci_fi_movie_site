# import the movieSite class here
import media
import fresh_tomato

# you dont need to add self, instead add all the other arguments

toy_story = media.Movie("Toy Story", "A story of a boy and his toys come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4")

avatar = media.Movie("Avatar", "A marine on an alien planet",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn","https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris", "https://static.rogerebert.com/uploads/movie/movie_poster/ratatouille-2007/large_taAPNsf6G4EXBYSG7Jyvd9HHKnH.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", "An author meets historical figures in Paris", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=dtiklALGz20")
hunger_games = media.Movie("Hunger Games", "A survival story in a futuristic universe", "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF8")


# movies list
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# call open_movies_page
fresh_tomato.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
