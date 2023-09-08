from django.shortcuts import render
from beranda.models import Daftar
# Create your views here.

def dashboard(request):
    regis = Daftar.objects.all()
    context ={
        'title':'Dashboard',
        'regis':regis
    }
    return render(request,'backend/dashboard.html',context)