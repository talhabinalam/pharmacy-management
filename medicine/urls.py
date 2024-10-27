from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('all_medicines/', AllMedicinesView.as_view(), name='all_medicines'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', login_required(LogoutView.as_view()), name='logout'),
]
