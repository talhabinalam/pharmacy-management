from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from medicine.models import Medicine
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        medicines = Medicine.objects.all()
        paginator = Paginator(medicines, 5)  # Show 5 medicines per page.

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
        query = request.GET.get('q')
        medicines = Medicine.objects.all()

        if query:
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
        return render(request, 'search-results.html', context)


class MedicinesListView(View):
    def get(self, request):
        medicines = Medicine.objects.all()
        return render(request, 'medicines-list.html', {'medicines': medicines})


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


class AddOrEditMedicineView(View):
    def get(self, request, medicine_id=None):
        medicine = None
        if medicine_id:
            medicine = get_object_or_404(Medicine, id=medicine_id)
        return render(request, 'add-medicine.html', {'medicine': medicine})

    def post(self, request, medicine_id=None):
        name = request.POST.get('name')
        generic_name = request.POST.get('generic_name')
        manufacturer = request.POST.get('manufacturer')
        description = request.POST.get('description')
        price = request.POST.get('price')
        batch_number = request.POST.get('batch_number')

        if medicine_id:  # Editing
            medicine = get_object_or_404(Medicine, id=medicine_id)
            medicine.name = name
            medicine.generic_name = generic_name
            medicine.manufacturer = manufacturer
            medicine.description = description
            medicine.price = price
            medicine.batch_number = batch_number
            medicine.save()
            messages.success(request, "Medicine updated successfully!")
        else:  # Adding
            Medicine.objects.create(
                name=name,
                generic_name=generic_name,
                manufacturer=manufacturer,
                description=description,
                price=price,
                batch_number=batch_number
            )
            messages.success(request, "Medicine added successfully!")
            return redirect('add-medicine')

        return redirect('medicines-list')


class DeleteMedicineView(View):
    def post(self, request, medicine_id):
        medicine = get_object_or_404(Medicine, id=medicine_id)
        medicine.delete()
        messages.success(request, "Medicine deleted successfully!")
        return redirect('medicines-list')  # Redirect to the medicines list page



