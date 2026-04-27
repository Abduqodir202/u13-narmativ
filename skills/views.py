from django.shortcuts import render, redirect

from skills.forms import SkillsForm
from skills.models import Skills


# Create your views here.
def skills_list(request):
   skills = Skills.objects.all()
   return render(request,'skills/list.html',{'skills':skills})

def skills_create(request):
    form = SkillsForm()
    return render(request, 'skills/create.html', context={'form':form})

def skills_create_save(request):
    form = SkillsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('skills_list')
    return render(request,'skills/create.html', {'form':form})

def skills_create_update(request, pk=None):
    skill= Skills.objects.get(id=pk)
    form = SkillsForm(request.POST, instance=skill)
    return render(request,'skills/update.html',{'form':form,'s':skill})

def skills_update(request,pk=None):
    skill = Skills.objects.get(id=pk)
    form = SkillsForm(request.POST,instance=skill)
    if form.is_valid():
        form.save()
        return redirect('skills_list')
    return render(request,'skills/update.html',{'form':form,'s':skill})