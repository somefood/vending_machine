from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import VendingMachine


class VendingIndexView(ListView):
    model = VendingMachine
    template_name = 'vending/index.html'


class VendingDetailView(DetailView):
    model = VendingMachine
    template_name = 'vending/detail.html'
    context_object_name = "vm"

