from django.contrib import admin
from .models import VendingMachine, VendingItem


class VendingItemInline(admin.TabularInline):
    model = VendingItem


@admin.register(VendingMachine)
class VendingAdmin(admin.ModelAdmin):
    inlines = [
        VendingItemInline,
    ]