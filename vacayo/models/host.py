from django.contrib.gis.db import models
from django.conf import settings


class Host(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='host', unique=True)
    properties = models.ManyToManyField('Property', related_name='hosts')
    accepted_agreement_on = models.DateTimeField(null=True, blank=True)
    location = models.OneToOneField('Location')
    radius = models.IntegerField(null=True, blank=True, default=5)
    active = models.BooleanField(default=True)

    def to_dict(self):
        return {
            'accepted_agreement_on': self.accepted_agreement_on,
            'radius': self.radius,
            'location': self.location.to_dict(),
            'active': self.active
        }

    def __unicode__(self):
        return 'Host <{}>'.format(self.user.email)

    class Meta:
        db_table = 'host'
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'
