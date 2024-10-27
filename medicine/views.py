from django.shortcuts import render
from django.views import View
from medicine.models import Medicine
from django.core.paginator import Paginator

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
