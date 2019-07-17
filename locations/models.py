from django.contrib.gis.db import models


class FoodLocation(models.Model):
    name = models.CharField(max_length=256)
    # type = models.ForeignKey('FoodLocationType', on_delete=models.PROTECT)
    type = models.CharField(max_length=256, null=True)
    # date_from = models.DateField()
    # date_to = models.DateField()

    open_from = models.CharField(max_length=100, null=True, blank=True)
    open_to = models.CharField(max_length=100, null=True, blank=True)

    published = models.BooleanField(default=True)

    # Operation Times
    open_time1 = models.TimeField(blank=True, null=True)
    close_time1 = models.TimeField(blank=True, null=True)
    open_time2 = models.TimeField(blank=True, null=True)
    close_time2 = models.TimeField(blank=True, null=True)

    sunday = models.BooleanField(blank=True, null=True)
    monday = models.BooleanField(blank=True, null=True)
    tuesday = models.BooleanField(blank=True, null=True)
    wednesday = models.BooleanField(blank=True, null=True)
    thursday = models.BooleanField(blank=True, null=True)
    friday = models.BooleanField(blank=True, null=True)
    saturday = models.BooleanField(blank=True, null=True)

    # Subsidies, scores, etc
    snap = models.BooleanField(null=True, default=False)
    wic = models.BooleanField(null=True, default=False)
    fmnp = models.BooleanField(null=True, default=False)
    fresh_produce = models.BooleanField(null=True, default=False)
    mrfei_score = models.IntegerField(null=True, default=False)
    food_bucks = models.BooleanField(null=True, default=False)

    open_to_spec_group = models.BooleanField(
        'Open to Specific Group',
        null=True,
        blank=True
    )

    # Location
    address = models.CharField(null=True, max_length=256)
    street_one = models.CharField(null=True, max_length=256)
    street_two = models.CharField(null=True, max_length=256)
    city = models.CharField(null=True, max_length=256)
    state = models.CharField(null=True, max_length=256)
    zip_code = models.CharField(null=True, max_length=256)
    location_description = models.TextField(null=True)

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    point = models.PointField(blank=True, null=True)

    def __str__(self):
        return self.name