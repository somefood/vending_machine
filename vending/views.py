from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from .models import VendingMachine, VendingItem


class VendingIndexView(ListView):
    model = VendingMachine
    template_name = 'vending/index.html'


class VendingDetailView(DetailView):
    model = VendingMachine
    template_name = 'vending/detail.html'
    context_object_name = "vm"


def item_update_view(request, pk):
    if request.method == "POST":
        item = get_object_or_404(VendingItem, pk=pk)
        item.quantity -= 1
        item.save()
        vm = item.vending_machine
    return redirect(vm)
