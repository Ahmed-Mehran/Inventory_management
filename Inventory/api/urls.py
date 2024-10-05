from django.urls import path

from Inventory.api import views

urlpatterns = [
    
    path('inventory-list', views.InventoryListAV.as_view(), name='inventory-list'),
    
    path('inventory-details/<int:pk>', views.InventoryDetailsAV.as_view(), name='inventory-details'),
    
    
    
]
