# import class movie
# data points- title, youtubeTrailer, storyline, reviews, posterImage
#show tralier function

import webbrowser

# to name a class
class Movie():
	# double dash - special reserved function or method in python
	# initializes a new memory space
	# self is the object being created when you call the method
	# self is added by default
	
	'''This class provides a way to store movie related information'''
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	# constructor
	def __init__(self, movie_title, youtube_trailer):
		# using omdbapi to get movie details
		omdb_base_url = "http://www.omdbapi.com/" 
		query_by_title = "?t=" + movie_title
		movies_url = omdb_base_url + query_by_title
		get_movie_data = urllib2.urlopen(movies_url)
		json_data = json.loads(get_movie_data)

		print json_data

		self.title = json_data["Title"]
		self.genre = json_data["Genre"]
		self.year = json_data["Released"][-4:] #get four digit year
		self.storyline = json_data["Plot"]
		self.poster_image_url = json_data["Poster"]
		self.imdb_rating = json_data["imdbRating"]
		self.trailer_youtube_url = youtube_trailer

    # instance method
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
