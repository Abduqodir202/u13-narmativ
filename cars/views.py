from django.shortcuts import render

# Create your views here.

def car_list(request):
    return render(request,'cars/list.html')
