import urllib2
import json

# get api keys and url's, global, needs updating
tmb_api_key = "4a56086013810376ea1cc0c7f8e5b45c"
id_science_fiction = 878
base_tmb_url = "https://api.themoviedb.org/3"

# search by movie id
# tmb_url_by_movie_id = base_tmb_url + "/movie/" + {movie_id}
# search by genre
tmb_url_by_genre = base_tmb_url + "/genre/{tmb_id}/movies?api_key={tmb_api_key}"

def tmb_movie_search_by_genre(query_id,api_key):
	api_key = tmb_api_key

	# search by genre
	url = tmb_url_by_genre.format(tmb_id=query_id,tmb_api_key=api_key)

	# add any query
	default_query = "&language=en-US&include_adult=true&sort_by=created_at.asc&page=1"

	url = url + default_query

	# api_call-for raw data
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	movie_results = data["results"]
	
	# datapoints- name, description, image, youtubeLink, rating
	# movies of voter-rating above 7
	count = 0
	tmb_base_image_path = "https://image.tmdb.org/t/p/w300"
	for entry in movie_results:
		if entry["vote_average"] > 7:
			count += 1
			id = str(entry["id"])
			title = entry["title"]
			description = entry["overview"]
			poster_img_path = tmb_base_image_path + entry["poster_path"]
			
			# api call for youtube video links
    print "clicked and done"
	# print count

# genre- science fiction, id=878, name- Science Fiction
tmb_movie_search_by_genre(id_science_fiction,tmb_api_key)