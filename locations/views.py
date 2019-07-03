from .models import FoodLocation
from .serializers import FoodLocationGETSerializer, FoodLocationGeoSerializer
from rest_framework import viewsets


class FoodLocationsViewSet(viewsets.ModelViewSet):
    """ Viewset for Food Locations """
    queryset = FoodLocation.objects.filter(published=True)

    def get_serializer_class(self):
        # todo: handle POST requests -- will likely need own serializer
        response_format = self.request.query_params.get('format', 'json')

        if response_format == 'geojson':
            return FoodLocationGeoSerializer

        return FoodLocationGETSerializer

