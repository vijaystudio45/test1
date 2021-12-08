from django.db import models


class dbFileds(models.Model):
    distance = models.IntegerField(max_length=500, null=True)
    title = models.CharField(max_length=500, null=True)
    run_date = models.DateField(null=False, auto_now_add=False)

    class Meta:
        db_table = 'allowed_fields'
# Create your models here.
