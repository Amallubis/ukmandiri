from django.urls import path
from backend import views 

urlpatterns = [
    path('backend/', views.dashboard, name='dashboard'),
    path('detail/', views.detail_daftar, name='detail'),
    path('delete_detail/<id_detail>', views.delete_detail, name='delete'),
    path('buat-promosi/', views.buat_promosi, name='buat-promosi'),
    path('edit-promosi/<int:id_promosi>/', views.edit_promosi, name='edit-promosi'),
    path('hapus-promosi/<int:id_promosi>/', views.hapus_promosi, name='hapus-promosi'),
    path('detail-promosi/', views.detail_promosi, name='detail-promosi'),
    path('export/xls/', views.export_xls, name='export_xls'),
    #pengurus
    path('detail-pengurus/', views.detail_pengurus, name='detail-pengurus'),
    path('add-pengurus/', views.add_pengurus, name='add-pengurus'),
    path('edit-pengurus/<int:id_edit>/', views.edit_pengurus, name='edit-pengurus'),
    path('delete-pengurus/<int:id_delete>/', views.delete_detail, name='delete-pengurus'),
    #Profil
    path('profil/', views.profil, name='profil'),
    
    
]
