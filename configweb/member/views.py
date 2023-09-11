from django.shortcuts import render
from django.contrib import messages
from member.models import Member
from member.forms import FormAddMember

# Create your views here.

def add_member(request):
    if request.POST:
        form = FormAddMember(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request,'Data Anda Berhasil dikirim')
            form = FormAddMember()
            context ={
                'title':'Daftar Anggota',
                'form':form
            }
            return render(request,'member/add-member.html',context)
    else:
        form = FormAddMember()
        return render(request,'member/add-member.html',{'form':form})