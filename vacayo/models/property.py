from django.db import models

ONBOARDING_STATUS = [
    ('pending_review', 'Pending Review'),
    ('pending_site_visit', 'Pending Site Visit'),
    ('pending_lease_signing', 'Pending Lease Signing'),
    ('ready', 'Ready'),
]

class Property(models.Model):
    address1 = models.CharField(max_length=256, db_index=True)
    address2 = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    state = models.CharField(max_length=256, blank=True, null=True)
    zip_code = models.CharField(max_length=256, blank=True, null=True)
    bedrooms = models.DecimalField(decimal_places=1, max_digits=3, blank=True, null=True)
    bathrooms = models.DecimalField(decimal_places=1, max_digits=3, blank=True, null=True)
    home_type = models.CharField(max_length=256, blank=True, null=True)
    home_size = models.IntegerField(blank=True, null=True)
    available_date = models.DateField(blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)
    last_rent = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    offer = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    main_image = models.ImageField(upload_to='images/properties', blank=True, null=True)
    status = models.CharField(max_length=256, choices=ONBOARDING_STATUS, default='pending_review')

    def __unicode__(self):
        return '{}, {}, {} {}'.format(self.address1, self.city, self.state, self.zip_code)

    @property
    def onboarding_statuses(self):
        def find(s):
            return next((i for i, x in enumerate(ONBOARDING_STATUS) if x[0] == s), [None])

        return [{
            'name': name,
            'is_done': bool(find(self.status) >= find(name)),
            'is_current': bool(find(self.status) == find(name))
        } for (name, human_name) in ONBOARDING_STATUS]

    class Meta:
        db_table = 'property'
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
