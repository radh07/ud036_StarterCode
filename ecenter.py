import fresh_tomatoes
import media
from urllib2 import Request, urlopen
import json

# Make an API call to OMDb to get year of release and plot line.
def get_movie_info(imdb_api_url):
	request = Request(imdb_api_url)
	response = urlopen(request)
	movieinfo = json.loads(response.read())
	return movieinfo['Year'], movieinfo['Plot']

# Movie 1 - Rain Man
rainman_year, rainman_plot = get_movie_info(
"http://www.omdbapi.com/?t=Rain+Man&y=&plot=short&r=json")
rainman = media.Movie("Rain Man", rainman_year, rainman_plot, 
"https://upload.wikimedia.org/wikipedia/en/b/b2/Rain_Man_poster.jpg", 
"https://www.youtube.com/watch?v=aJlbq6YVGV0")

# Movie 2 - Ferris Bueller's Day Off
fbdo_year, fbdo_plot = get_movie_info(
"http://www.omdbapi.com/?t=Ferris+Bueller's+Day+Off&y=&plot=short&r=json")
fbdo = media.Movie("Ferris Bueller's Day Off", fbdo_year, fbdo_plot, 
"https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg", 
"https://www.youtube.com/watch?v=iqyxxMFOFa0")

# Movie 3 - Back To The Future
btof_year, btof_plot = get_movie_info(
"http://www.omdbapi.com/?t=back+to+the+future&y=&plot=short&r=json")
btof = media.Movie("Back to the future", btof_year, btof_plot, 
"https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg", 
"https://www.youtube.com/watch?v=qvsgGtivCgs")

# Create a list of movies to display on website
movies = [rainman, fbdo, btof]
# Write the html content and open the web page
fresh_tomatoes.open_movies_page(movies)



