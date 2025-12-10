from django import forms
from .models import Mahasiswa

# ✅ Menggunakan ModelForm supaya bisa dipakai untuk tambah & edit data
class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['nama', 'npm', 'email', 'whatsapp', 'pendidikan_terakhir', 'jurusan', 'tempat_lahir', 'tanggal_lahir', 'alamat']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama mahasiswa'}),
            'npm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan NPM'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan email mahasiswa'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan nomor whatsapp'}),
            'pendidikan_terakhir': forms.Select(attrs={'class': 'form-select form-select-plain'}),
            'jurusan': forms.Select(attrs={'class': 'form-select form-select-plain'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kota lahir'}),
            'tanggal_lahir': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Alamat lengkap', 'rows': 2}),
        }
        labels = {
            'nama': 'Nama Lengkap',
            'npm': 'NPM',
            'email': 'Email',
            'whatsapp': 'WhatsApp / Telepon',
            'pendidikan_terakhir': 'Pendidikan Terakhir',
            'jurusan': 'Jurusan',
            'tempat_lahir': 'Tempat Lahir',
            'tanggal_lahir': 'Tanggal Lahir',
            'alamat': 'Alamat',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pastikan ada placeholder pilihan yang jelas untuk select
        try:
            pk_choices = list(self.fields['pendidikan_terakhir'].choices)
            if not pk_choices or (pk_choices and pk_choices[0][0] != ''):
                self.fields['pendidikan_terakhir'].choices = [('', '— Pilih Pendidikan —')] + pk_choices
        except Exception:
            pass

        try:
            jr_choices = list(self.fields['jurusan'].choices)
            if not jr_choices or (jr_choices and jr_choices[0][0] != ''):
                self.fields['jurusan'].choices = [('', '— Pilih Jurusan —')] + jr_choices
        except Exception:
            pass
