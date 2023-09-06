from django.shortcuts import render

# Create your views here.

def beranda(request):
    context ={
        'title':'Beranda | UKMandiri'
    }
    return render(request,'beranda/beranda.html',context) 