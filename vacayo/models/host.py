from django.db import models
from django.conf import settings

class Host(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='host', unique=True)
    properties = models.ManyToManyField('Property', related_name='hosts')
    accepted_agreement_on = models.DateTimeField(null=True, blank=True)
    manage_radius = models.IntegerField(null=True, blank=True, default=5)
    manage_address = models.CharField(null=True, blank=True, max_length=1024)
    active = models.BooleanField(default=True)

    def to_dict(self):
        return {
            'accepted_agreement_on': self.accepted_agreement_on,
            'manage_radius': self.manage_radius,
            'manage_address': self.manage_address,
            'active': self.active
        }

    def __unicode__(self):
        return 'Host <{}>'.format(self.user.email)

    class Meta:
        db_table = 'host'
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'
