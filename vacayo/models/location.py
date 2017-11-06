from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Location(models.Model):
    _address = models.CharField(max_length=1024, blank=True, null=True, db_index=True)
    address1 = models.CharField(max_length=256, blank=True, null=True)
    address2 = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True, db_index=True)
    state = models.CharField(max_length=256, blank=True, null=True, db_index=True)
    zip_code = models.CharField(max_length=256, blank=True, null=True, db_index=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    geo = models.PointField(geography=True, blank=True, null=True)
    needs_review = models.BooleanField(default=False)

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if address is None:
            del self.address
            return

        from ..services.property import PropertyService
        property_service = PropertyService()

        self._address = address

        # attempt to geolocate
        try:
            lat, lng = property_service.geolocate(address)
            self.latitude = lat
            self.longitude = lng
        except (Exception,) as e:
            self.needs_review = True

        # attempt to parse
        try:
            address = property_service.parse(address)
            self.address1 = address.get('address1')
            self.address2 = address.get('address2')
            self.city = address.get('city')
            self.state = address.get('state')
            self.zip_code = address.get('zip_code')
        except (Exception,) as e:
            self.needs_review = True

    @address.deleter
    def address(self):
        self._address = None
        self.address1 = None
        self.address2 = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.latitude = None
        self.longitude = None
        self.needs_review = None

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.geo = Point(self.latitude, self.longitude, srid=4326) if self.latitude and self.longitude else None

        super(Location, self).save(force_insert, force_update, using, update_fields)

    def to_dict(self):
        return {
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    def __unicode__(self):
        return self.address or ''

    class Meta:
        db_table = 'location'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
