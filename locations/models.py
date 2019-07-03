from django.contrib.gis.db import models


class FoodLocation(models.Model):
    name = models.CharField(max_length=256)
    # type = models.ForeignKey('FoodLocationType', on_delete=models.PROTECT)
    type = models.CharField(max_length=256)
    # date_from = models.DateField()
    # date_to = models.DateField()

    open_from = models.CharField(max_length=10)
    open_to = models.CharField(max_length=10)

    published = models.BooleanField(default=True)

    # Operation Times
    open_time = models.TimeField()
    close_time = models.TimeField()

    sunday = models.BooleanField()
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()

    # Subsidies, scores, etc
    snap = models.BooleanField(null=True, default=False)
    wic = models.BooleanField(null=True, default=False)
    fmnp = models.BooleanField(null=True, default=False)
    fresh_produce = models.BooleanField(null=True, default=False)
    mrfei_score = models.IntegerField(null=True, default=False)
    food_bucks = models.BooleanField(null=True, default=False)

    # Location
    address = models.CharField(null=True, max_length=256)
    street_one = models.CharField(null=True, max_length=256)
    street_two = models.CharField(null=True, max_length=256)
    city = models.CharField(null=True, max_length=256)
    state = models.CharField(null=True, max_length=256)
    zip_code = models.CharField(null=True, max_length=256)
    location_description = models.TextField(null=True)

    latitude = models.BooleanField(null=True)
    longitude = models.BooleanField(null=True)
    point = models.PointField(null=True)

    def __str__(self):
        return self.name