from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.conf import settings


class Host(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='host', unique=True)
    properties = models.ManyToManyField('Property', related_name='hosts')

    active = models.BooleanField(default=True)
    accepted_agreement_on = models.DateTimeField(null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=1024)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    radius = models.IntegerField(null=True, blank=True, default=5)
    geo = models.PointField(geography=True, null=True, blank=True)

    @property
    def location(self):
        return {
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    @location.setter
    def location(self, location):
        self.address = location['address']
        self.latitude = location['latitude']
        self.longitude = location['longitude']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.geo = Point(self.latitude, self.longitude, srid=4326) if self.latitude and self.longitude else None

        super(Host, self).save(force_insert, force_update, using, update_fields)

    def to_dict(self):
        return {
            'accepted_agreement_on': self.accepted_agreement_on,
            'radius': self.radius,
            'location': self.location,
            'active': self.active
        }

    def __unicode__(self):
        return 'Host <{}>'.format(self.user.email)

    class Meta:
        db_table = 'host'
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'
