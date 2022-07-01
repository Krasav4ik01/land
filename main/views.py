from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def form(request):
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST)
    #     if form.is_valid():
    #         profile = form.save(commit=False)
    #         # profile.user = request.user
    #         profile.save()
    # else:
    #     form = ProfileForm()
    return render(request,'main/form.html')
def example(request):
    if request.method == 'POST':

        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/POST/')


    else:
        form = ProfileForm()

    return render(request,'main/example.html',{'form':form})


