

from django.shortcuts import render

# Create your views here.
def mainaction(request):
     return render(request,'main_page.html')

