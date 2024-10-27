from django.shortcuts import render, redirect
from django.views import View
from medicine.models import Medicine
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):
    def get(self, request):
        medicines = Medicine.objects.all()
        paginator = Paginator(medicines, 5)  # Show 5 contacts per page.

        user = request.user

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'user': user,
                   }
        return render(request, 'index.html', context)


class SearchView(View):
    def get(self, request):
        query = request.GET.get('q')  # Get the search query from the request
        medicines = Medicine.objects.all()

        if query:  # Check if there is a search keyword
            # Use Q to filter based on case-insensitive search for name or generic name
            medicines = medicines.filter(
                Q(name__icontains=query) |
                Q(generic_name__icontains=query)
            )
            # print(f"Query: {query}, Results found: {medicines.count()}")

        else:
            medicines = Medicine.objects.none()
            print("No search query provided.")

        context = {
            'medicines': medicines,
            'query': query
        }
        return render(request, 'search_results.html', context)


class AllMedicinesView(View):
    def get(self, request):
        medicines = Medicine.objects.all()
        return render(request, 'all_medicines.html', {'medicines': medicines})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'You must have superuser access!')
            return redirect('login')


class LogoutView(View):
    login_url = '/login/'
    def post(self, request):
        logout(request)
        return redirect('index')


class AddMedicineView(View):
    def post(self, request):
        if request.user.is_authenticated:
            medicine_name = request.POST.get('medicine_name')
