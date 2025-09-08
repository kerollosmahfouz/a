from django.shortcuts import render
# from .models import cont
from .forms import contform

# Create your views here.

def h (request):
    return render(request, 'h.html')

def send (request):
    if request.method == 'POST':
        cont = contform(request.POST)
        if cont.is_valid():
            cont.save()
        # name = request.POST.get('name')
        # pnum = request.POST.get('pnum')
        # cont.objects.create(age = age2)

    return render(request,'h.html')