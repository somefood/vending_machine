from django.db import models


class VendingMachine(models.Model):
    name = models.CharField(max_length=30, verbose_name="자판기명")