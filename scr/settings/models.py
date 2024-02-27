from django.db import models

# Create your models here.

class Brand(models.Model):

    PRDName = models.CharField(verbose_name=("brand name"), max_length=50)
    PRDDesc = models.TextField(verbose_name=("description"),blank=True,null=True)


    def __str__(self):
        return self.PRDName


class Variant(models.Model):

    VARName = models.CharField(verbose_name=("brand name"), max_length=50)
    VARDesc = models.TextField(verbose_name=("description"),blank=True,null=True)


    def __str__(self):
        return self.VARName


