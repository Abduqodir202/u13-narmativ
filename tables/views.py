from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import Tables


def tables_list(request):
    search = request.GET.get('search', '')
    page_number = request.GET.get('page', 1)

    tables = Tables.objects.all()

    # 🔍 SEARCH
    if search:
        tables = tables.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    # 📄 PAGINATION
    paginator = Paginator(tables, 3)
    page_obj = paginator.get_page(page_number)

    return render(request, 'tables/list.html', {
        "page_obj": page_obj,
        "search": search
    })