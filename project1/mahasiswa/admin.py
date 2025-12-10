from django.contrib import admin
from .models import Mahasiswa


@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'npm', 'email', 'whatsapp', 'jurusan', 'pendidikan_terakhir')
    search_fields = ('nama', 'npm', 'email', 'jurusan')
    list_filter = ('pendidikan_terakhir', 'jurusan')
    readonly_fields = ()
