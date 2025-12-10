from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_mahasiswa, name='input_mahasiswa'),
    path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'),
    path('hapus/<int:id>/', views.hapus_mahasiswa, name='hapus_mahasiswa'),
    path('edit/<int:id>/', views.edit_mahasiswa, name='edit_mahasiswa'),
    path('export-excel/', views.export_excel, name='export_excel'),  # untuk simpan ke excel

]
