from django.urls import path
from . import views

app_name = "vending"
urlpatterns = [
    path('', views.VendingIndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.VendingDetailView.as_view(), name='detail'),
]