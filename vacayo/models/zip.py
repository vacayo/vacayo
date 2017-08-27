from django.db import models

class Zip(models.Model):
    code = models.CharField(max_length=256)
    in_service = models.BooleanField(default=True)

    def __unicode__(self):
        return '{}: {}'.format(self.code, self.in_service)

    class Meta:
        db_table = 'zip'
        verbose_name = 'Zip'
        verbose_name_plural = 'Zips'
