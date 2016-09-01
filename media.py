# Class definition for Movie

class Movie():
	""" This class contains information about movies including
	title, year released, plot, poster image url and trailer url.
	Year released and plot are obtained using API calls to OMDb.
	Poster image url is from WikiPedia and trailer url is from YouTube. 
	"""
	def __init__(self, movie_title, movie_year, movie_storyline, poster_image_url, 
	trailer_youtube_url):
		self.title = movie_title
		self.year = movie_year
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url