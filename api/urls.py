from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('contact/', views.contact_view, name='contact'),
     path('success/', views.success_view, name='success'),
]
