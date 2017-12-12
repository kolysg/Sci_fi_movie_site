# import class movie
# data points- title, youtubeTrailer, storyline, reviews, posterImage
#show tralier function
import urllib2
import json
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
		omdb_api_key = "6d65c0fb"
		omdb_base_url = "http://www.omdbapi.com/?apikey={api_key}&t={movie_title}" 
		# query_by_title = "&t=" + movie_title
		movie_url = omdb_base_url.format(api_key=omdb_api_key, movie_title=movie_title)
		movie_url = movie_url.replace(" ", "+")
		# print movie_url
		get_movie_data = urllib2.urlopen(movie_url)
		json_data = json.load(get_movie_data)


		# using youtube api to get trailer video - Todo
		# youtube_base_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=2" #max 2 results
		# query = "&q=" + movie_title
		# youtube_api_key = "AIzaSyBljuu-8XWjq3x1g_dCGxSyWFk29FzbvnY"

		self.title = json_data["Title"]
		self.genre = json_data["Genre"]
		self.year = json_data["Released"][-4:] #get four digit year
		self.storyline = json_data["Plot"]
		self.poster_image_url = json_data["Poster"]
		self.imdb_rating = json_data["imdbRating"]
		self.trailer_youtube_url = youtube_trailer
		self.imdb_id = json_data["imdbID"]

		# print json_data["Poster"]

    # instance method
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
