from django.shortcuts import render
from beranda.forms import FormDaftar
from django.contrib import messages
# Create your views here.

def beranda(request):
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
            return render(request,'beranda/beranda.html',context) 
    else:
        form = FormDaftar()
        return render(request,'beranda/beranda.html',{'form':form})

    
def daftar(request):
    context ={
        'title':'Daftar'
    }
    return render(request,'beranda/beranda.html',context)