# from django.shortcuts import render

# # Create your views here.
# def adminwelcomeaction(request):
#     return render(request,'adminwelcome.html')

from django.shortcuts import render
from .models import User

def admin_welcome(request):
    users = User.objects.all()
    return render(request, 'adminwelcome.html', {'users': users})

