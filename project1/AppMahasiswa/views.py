from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Selamat Datang di Aplikasi Mahasiswa</h1><p>Silakan akses <a href='/mahasiswa/input/'>halaman input mahasiswa</a></p>")
