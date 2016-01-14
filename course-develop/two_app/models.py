from django.db import models

# Create your models here.
class WebUser(models.Model):
    ip = models.GenericIPAddressField()
    pv = models.IntegerField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
