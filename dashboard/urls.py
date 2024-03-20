from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    path('create-category/',views.create_category,name='create-category'),
    path('list-category/',views.list_category,name='list-category'),
]
