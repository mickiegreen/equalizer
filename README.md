# Equalizer
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

## Pre installation
1. Python2.7 - This project has been built and tested with Python2.7.14
3. pip
2. yarn package manager
4. virtualenv
5. mysql server running

### setup dev
1. setup virtualenv
```
virtualenv env_name
```

2. activate virtualenv
```
source env_name/bin/activate 
```
3. install python required packages
```
pip install -r requirements
```
4. set up webapp dependencies
```
cd webapp
yarn
```
5. start webpack (webpack port configured to 3000)
```
yarn start
```

6. start django (configured to port 8000)
```
python manage.py migrate
python manage.py runserver
```
7. test server is up at 

    http://localhost:8000

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

# TODOs
1. build htmls
2. develop request handlers
3. css design
4. docs

## University servers
```
virtualenv equalizer
source equalizer/bin/activate.csh
git clone https://github.com/mickiegreen/EqualizerProject
cd EqualizerProject
pip install -r requirements.txt
cd webapp
python manage.py migrate
python manage.py runserver delta-tomcat-vm:40743
```


