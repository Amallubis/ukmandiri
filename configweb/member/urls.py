from django.urls import path
from member import views

urlpatterns = [
    path('add-member',views.add_member,name='add-member')
]
