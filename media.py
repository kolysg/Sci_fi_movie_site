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
	def __init__(self, movie_title, youtubeTrailer):
		# using omdbapi to get movie details
		omdb_base_url = "http://www.omdbapi.com/" 
		query_by_title = "?t=" + movie_title
		movies_url = omdb_base_url + query_by_title
		get_movie_data = urllib2.urlopen(movies_url)
		json_obj = json.loads(get_movie_data)

		print json_obj

		self.title = title
		self.storyline = storyline
		self.poster_image_url = posterImage
		self.trailer_youtube_url = youtubeTrailer

    # instance method
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
