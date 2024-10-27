from django.shortcuts import render
from django.views import View
from medicine.models import Medicine
from django.core.paginator import Paginator
from django.db.models import Q

class IndexView(View):
    def get(self, request):
        medicines = Medicine.objects.all()
        paginator = Paginator(medicines, 5)  # Show 5 contacts per page.

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj
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