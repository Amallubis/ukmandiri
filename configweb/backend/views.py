from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from beranda.models import Daftar
from backend.models import Promosi, Banner, Pengurus, Profil
from backend.forms import FormPromosi, FormBanner, FormPengurus, FormProfil
from django.contrib.auth.decorators import login_required
from django.conf import settings
from backend.resource import DaftarResource
from backend.resource import MemberResource

def export_member_xls(request):
    member = MemberResource()
    dataset = member.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=member.xls'
    return response

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
    jmlpengurus= Pengurus.objects.count()
    context ={
        'title':'Dashboard',
        'jumlah':jumlah,
        'promosi':promosi,
        'jmlpengurus':jmlpengurus
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





@login_required(login_url=settings.LOGIN_URL)
def detail_pengurus(request):
    pengurus =Pengurus.objects.all()
    return render(request,'backend/detail-pengurus.html',{'pengurus':pengurus})


@login_required(login_url=settings.LOGIN_URL)
def add_pengurus(request):
    if request.POST:
        form = FormPengurus(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil menambahkan pengurus')
            return render(request,'backend/add-pengurus.html',{'form':form})
    else:
        form = FormPengurus()
        return render(request,'backend/add-pengurus.html',{'form':form})

        
@login_required(login_url=settings.LOGIN_URL)
def edit_pengurus(request,id_edit):
    if request.POST:
        pengurus = Pengurus.objects.get(id = id_edit)
        form = FormPengurus(request.POST, request.FILES, instance=pengurus)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil di Update')
            form = FormPengurus(instance=pengurus)
            pengurus = Pengurus.objects.get(id=id_edit)
            return render(request,'backend/edit-pengurus.html',{'form':form,'pengurus':pengurus})
    else:
        pengurus = Pengurus.objects.get(id=id_edit)
        form = FormPengurus(instance=pengurus)
        return render(request,'backend/edit-pengurus.html',{'form':form,'pengurus':pengurus})


@login_required(login_url=settings.LOGIN_URL)
def delete_pengurus(request,id_delete):
    pengurus = Pengurus.objects.get(id=id_delete)
    pengurus.delete()
    return redirect('detail-pengurus')



def edit_profil(request):
    if request.POST:
        p = Profil.objects.get(pk=1)
        form = FormProfil(request.POST,request.FILES, instance=p) 
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            form = FormProfil(instance=p)
            return render(request,'backend/edit-profil.html',{'form':form})
    else:
        p = Profil.objects.get(pk=1)
        form = FormProfil(instance=p)
        return render(request,'backend/edit-profil.html',{'form':form})
    