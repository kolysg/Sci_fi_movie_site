# Sci-fi Movies

This is a python project I created for the Udacity Full Stack Web Developer Nanodegree.  It is a dynamically generated website that displays a list of my favourite sci-fi movies.

This utilizes the OMDb (Open Movie Database) API to get the info of each individual sci-fi movie title. The OMDb api requires an api key to access any api data. Video links for each title has been manually put since OMDb site currently doesn't support video link. 

Todo: To access youtube api for trailer-links. 

## Usage

Running `entertainment_center.py` creates a new instance of a `fresh_tomatoes.html`.

### Adding new movies

To add a movie, simply add a new movie instance of the Movie class to `entertainment_center.py`, like this:
```
my_movie_object = media.Movie("Movie_title, Youtube_link)
```
Append the new movie instance to the movies list.
```
movies = [..., 'some_movie','some_other_movie', ...]
```

The order the movies are added to the list is the order they will be displayed on the website.  

### Customization
I added few changes to html and CSS to style the page a little differently.
Enjoy!  Maybe you will find your new sci-fi favourite movie in this list!

### Todos
Playing with youtube api.
Create checks for missing data.
Changing styles for headers.