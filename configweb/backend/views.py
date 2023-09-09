from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from beranda.models import Daftar
from backend.models import Promosi, Banner
from backend.forms import FormPromosi, FormBanner
from django.contrib.auth.decorators import login_required
from django.conf import settings
from backend.resource import DaftarResource


def export_xls(request):
    daftar = DaftarResource()
    dataset = daftar.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment; filename=daftar.xls'
    return response
# Create your views here.
@login_required(login_url= settings.LOGIN_URL)
def dashboard(request):
    jumlah= Daftar.objects.count()
    promosi = Promosi.objects.count()
    context ={
        'title':'Dashboard',
        'jumlah':jumlah,
        'promosi':promosi
    }
    return render(request,'backend/dashboard.html',context)

    
@login_required(login_url=settings.LOGIN_URL)
def detail_daftar(request):
    daftar = Daftar.objects.all().order_by('-pk')
    context ={
        'title':'Detail',
        'daftar': daftar
    }
    return render(request,'backend/detail-daftar.html',context)

    
@login_required(login_url=settings.LOGIN_URL)
def delete_detail(request,id_detail):
    daftar = Daftar.objects.get(id = id_detail)
    daftar.delete()
    return redirect('detail') 
   
   
@login_required(login_url=settings.LOGIN_URL)
def buat_promosi(request):
    if request.POST:
        form = FormPromosi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Buat Promosi Berhasil')
            return render(request,'backend/buat-promosi.html',{'form':form})
    else:
        form = FormPromosi()
        return render(request,'backend/buat-promosi.html',{'form':form})

@login_required(login_url=settings.LOGIN_URL)
def edit_promosi(request,id_promosi):
    promosi = Promosi.objects.get(id = id_promosi)
    if request.POST:
        form = FormPromosi(request.POST, instance=promosi)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil mengubah promosi')
            form = FormPromosi(instance=promosi)
            return render(request,'backend/edit-promosi.html',{'form':form,'promosi':promosi})
    else:
        promosi = Promosi.objects.get(id = id_promosi)
        form = FormPromosi(instance=promosi)
        return render(request,'backend/edit-promosi.html',{'form':form, 'promosi':promosi})

        
@login_required(login_url=settings.LOGIN_URL)
def hapus_promosi(request,id_promosi):
    promosi = Promosi.objects.get(id = id_promosi)
    promosi.delete()
    messages.success(request,'Berhasil dihapus')
    return redirect('detail-promosi')

@login_required(login_url=settings.LOGIN_URL)
def detail_promosi(request):
    promosi = Promosi.objects.all()
    context ={
        'title':'Detail Promosi',
        'promosi':promosi
    }
    return render(request,'backend/detail-promosi.html',context)
        