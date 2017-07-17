from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Owner(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = PhoneNumberField()
    properties = models.ManyToManyField('Property')

    def __unicode__(self):
        return '{} {} <{}>'.format(self.first_name, self.last_name, self.email)

    class Meta:
        db_table = 'owner'
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'
