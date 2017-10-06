from django.db import models
from django.conf import settings

class Host(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='host')
    properties = models.ManyToManyField('Property', related_name='hosts')

    def __unicode__(self):
        return 'Host <{}>'.format(self.user.email)

    class Meta:
        db_table = 'host'
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'
