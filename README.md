# EqualizerProject
This repo contains final project of databases course.
Aims in creating an equalizer interface for searches
such that enable the searcher to "balance" the weights
he's giving to each of his search parameters.

## flow description
we used Youtube and Itunes Api's to get samples to our
database. Then we defined queries and database structure
that will give the best expected results from the sample.
This project also includes UI based on django with react
and graphql, which has been imported as described in 
*acknowledgments* section.

## Acknowledgments
1. For the GUI in subfolder webapp we used the awesome project 
from github as our infrastructure:

   https://github.com/jaffamonkey/reactjs-django-1

   written by *jaffamonkey*. 
   This infra has been adapted to our needs.
2. all other libraries are listed in requirements.txt

## Youtube & Itunes fields used from the Api:
```
duration # itunes
release_date # itunes
views # youtube
likes # youtube
comments # youtube
favorites # youtube
dislikes # youtube
track_name # itunes
artist_name # itunes
video_title # youtube
```

# TODOS


