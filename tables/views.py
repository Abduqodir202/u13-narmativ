from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from accounts.utils import login_required_custom
from tables.forms import TableModelForm
from tables.models import Tables


def tables_list(request):
    search = request.GET.get('search', '')
    page = request.GET.get('page')
    tables = Tables.objects.all()  # Queryset list [<booq1>.
    if search:
        tables = tables.filter(Q(title__icontains=search) | Q(description__icontains=search))
    paginator = Paginator(tables, 3)
    tables = paginator.get_page(page)
    return render(request, 'tables/list.html', {"tables": tables, 'search': search})


def tables_detail(request, pk):
    tables = Tables.objects.filter(id=pk).first()
    return render(request, 'tables/detail.html', {"tables": tables})


@login_required
def tables_create_form(request):
    form = TableModelForm()
    return render(request, 'tables/create.html', {"form": form})


@login_required
def tables_create(request):
    # data = request.POST
    # book = Books(title=data.get("title"), description=data.get("description"), price=data.get("price"))
    # book.save()
    # # Books.objects.create(title=data['title'], description=data['description'], price=data['price'])
    # return redirect('book_list')
    # form = BooksForm(request.POST)
    form = TableModelForm(request.POST)
    if form.is_valid():
        # data = form.cleaned_data
        # Books.objects.create(**data)
        form.save()
        return redirect('tables_list')
    return render(request, 'tables/create.html', {"form": form})



@login_required
def tables_update_forme(request, pk=None):
    table = Tables.objects.filter(id=pk).first()
    form = TableModelForm(instance=table)
    return render(request, 'tables/update.html', {"form": form, "table": table})


@login_required
def tables_update(request, pk=None):
    # Books.objects.filter(id=pk).update(title=request.POST.get("title"), description=request.POST.get("description"),
    #                                    price=request.POST.get("price"))
    table = Tables.objects.filter(id=pk).first()
    form = TableModelForm(instance=table, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('table_list')
    return render(request, 'tables/update.html', {"form": table, "table": table})


@login_required_custom
def tables_delete(request, pk=None):
    Tables.objects.filter(id=pk).delete()
    return redirect('tables_list')
