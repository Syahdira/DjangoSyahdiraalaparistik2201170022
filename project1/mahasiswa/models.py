# ket ini untuk model mhs
from django.db import models
# Pilihan pendidikan terakhir yang digunakan di form
PENDIDIKAN_CHOICES = [
    ('SD', 'SD'),
    ('SMP', 'SMP'),
    ('SMA', 'SMA/SMK'),
    ('D3', 'D3'),
    ('S1', 'S1'),
    ('S2', 'S2'),
    ('S3', 'S3'),
    ('Lainnya', 'Lainnya'),
]

# Pilihan jurusan
JURUSAN_CHOICES = [
    ('Pendidikan Biologi', 'Pendidikan Biologi'),
    ('Pendidikan Sejarah', 'Pendidikan Sejarah'),
    ('Pendidikan Geografi', 'Pendidikan Geografi'),
    ('Pendidikan Bahasa Inggris', 'Pendidikan Bahasa Inggris'),
    ('Pendidikan Matematika', 'Pendidikan Matematika'),
    ('Pendidikan BK', 'Pendidikan BK'),
    ('Pendidikan Sosiologi', 'Pendidikan Sosiologi'),
    ('Pendidikan Bahasa Indonesia', 'Pendidikan Bahasa Indonesia'),
    ('Pendidikan Ekonomi', 'Pendidikan Ekonomi'),
    ('Pendidikan Informatika', 'Pendidikan Informatika'),
    ('Pendidikan Fisika', 'Pendidikan Fisika'),
    ('Pendidikan IPS', 'Pendidikan IPS'),
    ('Pendidikan PPKn', 'Pendidikan PPKn'),
    ('Pendidikan Akuntansi', 'Pendidikan Akuntansi'),
    ('Biologi Terapan', 'Biologi Terapan'),
    ('Sains Data', 'Sains Data'),
    ('Teknologi Informasi', 'Teknologi Informasi'),
    ('Kewirausahaan', 'Kewirausahaan'),
    ('Studi Humanitas (S1)', 'Studi Humanitas (S1)'),
    ('Pasca Sarjana Studi Humanitas (S2)', 'Pasca Sarjana Studi Humanitas (S2)'),
    ('Pasca Sarjana Studi Lingkungan (S2)', 'Pasca Sarjana Studi Lingkungan (S2)'),
    ('Pasca Pendidikan Guru Vokasi (S2)', 'Pasca Pendidikan Guru Vokasi (S2)'),
    ('Pendidikan Profesi Guru', 'Pendidikan Profesi Guru'),
    ('Lainnya', 'Lainnya'),
]


class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=20)
    email = models.EmailField()
    # Nomor WhatsApp disimpan tanpa tanda + atau spasi (contoh: 6281234...)
    whatsapp = models.CharField(max_length=20, blank=True)
    # Alamat dan pendidikan terakhir
    alamat = models.TextField(blank=True)
    pendidikan_terakhir = models.CharField(max_length=20, blank=True, choices=PENDIDIKAN_CHOICES)
    # Jurusan dan Tempat/Tanggal Lahir
    jurusan = models.CharField(max_length=100, blank=True, choices=JURUSAN_CHOICES)
    tempat_lahir = models.CharField(max_length=100, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.nama} ({self.npm})"
