from django.http import HttpResponse

from game.forms import GameForm
from game.models import Game
from django.shortcuts import render, redirect

# Create your views here.
def game_list(request):
    game = Game.objects.all()
    return render(request,'game/list.html',{'game':game})

def game_create(request):
    form = GameForm()
    return render(request,'game/create.html',{'form':form})

def game_create_save(request):
    form = GameForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('game_list')
    return render(request,'game/create.html',{'form':form})


def game_update(request,pk=None):
    game = Game.objects.get(id=pk)
    form = GameForm(instance=game)
    return render(request,'game/update.html',{'form':form, 'game':game})

def game_update_save(request,pk=None):
    game = Game.objects.get(id=pk)
    form = GameForm(request.POST,instance=game)
    if form.is_valid():
        form.save()
        return redirect('game_list')
    return render(request,'game/update.html',{'form':form, 'game':game})

# def game_create_save(request):
#     return HttpResponse("Ishlayapti")


# def game_create_save(request):
#     if request.method == 'POST':
#         form = GameForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('game_list')
#         else:
#             print(form.errors)  # 👈 terminalda chiqadi
#     else:
#         form = GameForm()
#
#     return render(request, 'game/create.html', {'form': form})