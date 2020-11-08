from django.urls import path
from . import views

app_name="vending"

urlpatterns = [
    path('', views.VendingIndexView.as_view(), name='index'),
]