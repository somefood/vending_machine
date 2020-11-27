from django.urls import path
from . import views

app_name = "vending"
urlpatterns = [
    path('', views.VendingIndexView.as_view(), name='index'),
    path('detail/vm/<int:pk>/', views.VendingDetailView.as_view(), name='vm_detail'),
    path('detail/item/<int:pk>/', views.item_update_view, name='item_detail'),
]