from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers

from . import models


class FoodLocationGeoSerializer(geo_serializers.GeoFeatureModelSerializer):
    """ GeoJSON serializer for the `FoodLocation` model """

    class Meta:
        model = models.FoodLocation
        geo_field = "point"
        auto_bbox = True
        fields = '__all__'  # todo: explicitly define the fields


class FoodLocationGETSerializer(serializers.ModelSerializer):
    """ Serializer for GET requests made on `Food Location` model """

    class Meta:
        model = models.FoodLocation
        fields = '__all__'  # todo: explicitly define the fields

