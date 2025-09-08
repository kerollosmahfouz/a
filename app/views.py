from django.shortcuts import render
from .models import age

# Create your views here.

def h (request):
    return render(request, 'h.html')

def send (request):
    if request.method == 'POST':
        age2 = request.POST.get('age')
        age.objects.create(age = age2)

    return render(request,'h.html')