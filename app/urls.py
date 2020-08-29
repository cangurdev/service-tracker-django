from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment/', views.form, name='form'),
    path('device-status/', views.statusForm, name='statusForm'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
