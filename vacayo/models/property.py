from django.contrib.gis.db import models
from ..utils.enum import Enum

class ONBOARDING_STATUS(Enum):
    NEW = 'New'
    PENDING_REVIEW = 'Pending Review'
    PENDING_ASSIGNMENT = 'Pending Superhost Assignment'
    PENDING_VISIT = 'Pending Site Visit'
    PENDING_LEASE = 'Pending Lease Signing'
    READY = 'Ready'


class Property(models.Model):
    location = models.OneToOneField('Location')
    bedrooms = models.DecimalField(decimal_places=1, max_digits=3, blank=True, null=True)
    bathrooms = models.DecimalField(decimal_places=1, max_digits=3, blank=True, null=True)
    home_type = models.CharField(max_length=256, blank=True, null=True)
    home_size = models.IntegerField(blank=True, null=True)
    available_date = models.DateField(blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)
    last_rent = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    offer = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    main_image = models.ImageField(upload_to='images/properties', blank=True, null=True)
    status = models.CharField(max_length=256, choices=ONBOARDING_STATUS.choices(), default=ONBOARDING_STATUS.NEW)

    @property
    def onboarding_statuses(self):
        def find(s):
            return next((i for i, x in enumerate(ONBOARDING_STATUS.choices()) if x[0] == s), [None])

        return [{
            'name': name,
            'is_done': bool(find(self.status) >= find(name)),
            'is_current': bool(find(self.status) == find(name))
        } for (name, human_name) in ONBOARDING_STATUS.choices()]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        # Advance PENDING_REVIEW -> PENDING_ASSIGNMENT
        if self.status == ONBOARDING_STATUS.PENDING_REVIEW:
            if self.location.geo and self.offer:
                self.status = ONBOARDING_STATUS.PENDING_ASSIGNMENT

        # Advance PENDING_ASSIGNMENT -> PENDING_VISIT
        if self.status == ONBOARDING_STATUS.PENDING_ASSIGNMENT:
            if self.hosts.count():
                self.status = ONBOARDING_STATUS.PENDING_VISIT

        super(Property, self).save(force_insert, force_update, using, update_fields)

    def to_dict(self):
        return {
            'id': self.id,
            'offer': self.offer,
            'status': self.status,
            'location': self.location.to_dict(),
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'visit_date': self.visit_date.strftime('%m/%d/%Y') if self.visit_date else None,
            'main_image': self.main_image.url if self.main_image else 'https://placeimg.com/640/480/arch/grayscale',
            'onboarding_statuses': self.onboarding_statuses,
        }

    def __unicode__(self):
        return unicode(self.location)

    class Meta:
        db_table = 'property'
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
