from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('medicines_list/', MedicinesListView.as_view(), name='medicines-list'),
    path('update_medicines/', login_required(MedicinesListView.as_view()), name='update-medicines'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', login_required(LogoutView.as_view()), name='logout'),
    path('add_medicine/', login_required(AddOrEditMedicineView.as_view()), name='add-medicine'),
    path('edit_medicine/<int:medicine_id>/', login_required(AddOrEditMedicineView.as_view()), name='edit-medicine'),
    path('delete_medicine/<int:medicine_id>/', login_required(DeleteMedicineView.as_view()), name='delete-medicine'),
]