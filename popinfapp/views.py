from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
   if request.method == 'POST':
      pop= Information()
      pop.fullname = request.POST['fullname']
      pop.phone = request.POST['phone']
      pop.age = request.POST['age']
      pop.gender = request.POST['gender']
      pop.provence = request.POST['provence']
      pop.familymembers = request.POST['familymembers']
      pop.save()
   return render(request, 'index.html')