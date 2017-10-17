from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Owner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='owner', null=True, blank=True)
    properties = models.ManyToManyField('Property', related_name='owners')
    phone = PhoneNumberField()

    def __unicode__(self):
        return 'Owner <{}>'.format(self.user.email)

    class Meta:
        db_table = 'owner'
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'
