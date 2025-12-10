from django.contrib import admin
from django.urls import path, include
from AppMahasiswa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('', views.index, name='index'),
]
