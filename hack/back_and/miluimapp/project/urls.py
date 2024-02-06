from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('api/addresses/', views.get_addresses_and_id, name="get addresses and id"),
    path('api/miluimnik/<int:id>', views.get_name_and_family_name, name="get name and family name"),
    path('api/miluimnik/', views.add_business, name='add business')
]