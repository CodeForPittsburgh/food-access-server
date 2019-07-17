# Food Access Map server

This will host the api that will provide data to the food access map.

### Setting up virtualenv


### To install:
1. Clone this bad-boy  
`git clone https://github.com/CodeForPittsburgh/food-access-server.git`  
`cd food-access-server`  
2. move to the cloned directory  
`cd food-access-server`  
3. Setup virtual environment and install require
`pip install virtualenv`  
`virtualenv env -p python3   # creates virtual environment`  
`. env/bin/activate   # activates the virtual environment`  
`pip install -r requirements`
4. Install the dependencies  
`pip install -r requirements.txt` 
5. Set up a postgres database with PostGIS -  [instructions](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/postgis/)  
6. Modify and rename `food_access_backend/local_settings.py.example` per comments in that file
7. Migrate the models to your newly created db  
`python manage.py migrate`
8. Run the development server  
`python manage.py runserver`
9. You can add some sample data like this:  
`python manage.py load_csv sample.tsv`