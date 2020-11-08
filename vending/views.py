from django.shortcuts import render
from django.views.generic import TemplateView


class VendingIndexView(TemplateView):
    template_name = 'vending/index.html'