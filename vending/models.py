from django.db import models
from django.urls import reverse


class VendingMachine(models.Model):
    name = models.CharField(max_length=30, verbose_name="자판기명")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('vending:detail', args=[self.id])

    class Meta:
        verbose_name = '자판기'
        verbose_name_plural = '자판기'


class VendingItem(models.Model):
    vending_machine = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="상품명")
    quantity = models.PositiveIntegerField(default=0, verbose_name="수량")
    price = models.PositiveIntegerField(default=0, verbose_name="가격")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품'