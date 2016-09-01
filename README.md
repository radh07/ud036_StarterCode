This folder contains source code for a Movie Trailer website.
media.py -> contains class definition for a Movie class that has the following info:
* Title
* Year of release (from OMDb)
* Plot (from OMDb)
* Movie poster url (from Wikipedia)
* Movie trailer url (from YouTube)
        
ecenter.py -> creates a list containing multiple instances of the Movie class which are created using API calls to OMDb. Then it calls a method in fresh_tomatoes.py to create and open a web page.

fresh_tomatoes.py -> has a method that takes in a list of Movie class objects and creates a web page with information for every movie in the list. Each movie has the poster image with movie title and year, which, on mouseover, shows the plot. On clicking the image, the YouTube trailer is played as a modal window.

To run this project, download the three .py files and run "python ecenter.py" in Terminal.
