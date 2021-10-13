from django.shortcuts import render
from .forms import RegisterUser,Contact
# Create your views here.

def home_activity(request):
    fm=RegisterUser()
    fc=Contact()
    data={'form':fm ,'fc':fc}
    return render(request, 'index.html',data)