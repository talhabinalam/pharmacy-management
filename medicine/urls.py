from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('all_medicines/', AllMedicinesView.as_view(), name='all_medicines'),
]
