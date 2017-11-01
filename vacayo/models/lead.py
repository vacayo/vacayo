from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Lead(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = PhoneNumberField()
    location = models.OneToOneField('Location')

    def __unicode__(self):
        return 'Lead <{}>'.format(self.email)

    class Meta:
        db_table = 'lead'
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
