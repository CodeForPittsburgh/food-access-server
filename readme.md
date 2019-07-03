# Food Access Map server

This will host the api that will provide data to the food access map.

### To install:
1. Clone this bad-boy  
`git clone https://github.com/CodeForPittsburgh/food-access-server.git`
2. move to the cloned directory  
`cd food-access-server`
3. Install the dependencies  
`pip install -r requirements.txt` 
4. Set up a postgres database with PostGIS -  [instructions](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/postgis/)  
5. Modify and rename `food_access_backend/local_settings.py.example` per comments in that file
6. Migrate the models to your newly created db  
`python manage.py migrate`
7. Run the development server  
`python manage.py runserver`
8. You can add some sample data like this:  
`python manage.py load_csv sample.tsv`