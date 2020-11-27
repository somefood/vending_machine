from django.db import models
from django.urls import reverse
import random


def set_hex_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


class VendingMachine(models.Model):
    name = models.CharField(max_length=30, verbose_name="자판기명")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('vending:vm_detail', args=[self.id])

    class Meta:
        verbose_name = '자판기'
        verbose_name_plural = '자판기'


class VendingItem(models.Model):
    vending_machine = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="상품명")
    quantity = models.PositiveIntegerField(default=0, verbose_name="수량")
    price = models.PositiveIntegerField(default=0, verbose_name="가격")
    color = models.CharField(max_length=30, blank=True, verbose_name='색상')

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not getattr(self, 'color'):
            self.color = set_hex_color()
        super().save(*args, **kwargs)

    def get_absolute_rul(self):
        return reverse('vending:item_detail', args=[self.id])

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품'