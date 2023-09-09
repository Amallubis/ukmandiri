from django.shortcuts import render
from django.contrib import messages
from beranda.forms import FormDaftar
from backend.models import Promosi
# Create your views here.

def beranda(request):
    promosi = Promosi.objects.all().order_by('-pk')
    if request.POST:
        form = FormDaftar(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request,'Terimakasih, Kami akan memverifikasi Data Anda terlebih dahulu')
            form = FormDaftar()
            context ={
                'title':'Beranda | UKMandiri',
                'form':form,
                'promosi':promosi
                }
            return render(request,'beranda/beranda.html',context) 
    else:
        promosi = Promosi.objects.all().order_by('-pk')
        form = FormDaftar()
        return render(request,'beranda/beranda.html',{'form':form,'promosi':promosi})

    
def daftar(request):
    if request.POST:
        form = FormDaftar(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request,'Terimakasih, Kami akan memverifikasi Data Anda terlebih dahulu')
            form = FormDaftar()
            context ={
                'title':'Beranda | UKMandiri',
                'form':form,
                }
            return render(request,'beranda/daftar.html',context) 
    else:
        form = FormDaftar()
        return render(request,'beranda/daftar.html',{'form':form})