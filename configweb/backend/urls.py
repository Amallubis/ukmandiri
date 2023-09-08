from django.urls import path
from backend import views 

urlpatterns = [
    path('backend/', views.dashboard, name='dashboard')
]
