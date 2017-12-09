import urllib2
import json

# get api_key for the site- sent to my yahoomail
tmb_api_key = "4a56086013810376ea1cc0c7f8e5b45c"

tmb_url = "https://api.themoviedb.org/3/movie/"


def tmb_movie_search(query):
	api_key = tmb_api_key
	# search the api using movie_id
	# todo- search using title
	url = tmb_url + {movie_id} + "?api_key=" + tmb_api_key
	# replace space in the title
	movie_url = url.replace(' ', '%20')

	# add any query
	query = '?'
	final_movie_url = movie_url + query

	json_obj = urllib2.urlopen(final_movie_url)
	data = json.load(json_obj)

	# now loop through the data to find the necessary variables
	# name, description, a picture, movie_trailer_youtube_url

	# datapoints- name, description, image, youtubeLink, rating

