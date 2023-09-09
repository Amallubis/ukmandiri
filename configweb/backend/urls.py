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
    
]
