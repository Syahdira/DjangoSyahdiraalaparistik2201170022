from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import MahasiswaForm
from .models import Mahasiswa
from django.contrib.auth.decorators import login_required
import openpyxl

# ✅ Fungsi input (tambah data)
@login_required(login_url='/admin/login/')
def input_mahasiswa(request):
    pesan = ""
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            pesan = "Data mahasiswa berhasil disimpan."
            return redirect('daftar_mahasiswa')
    else:
        form = MahasiswaForm()

    return render(request, 'mahasiswa/input.html', {
        'form': form,
        'pesan': pesan,
    })


# ✅ Fungsi hapus data
@login_required(login_url='/admin/login/')
def hapus_mahasiswa(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)
    mhs.delete()
    return redirect('input_mahasiswa')


# ✅ Fungsi edit data
@login_required(login_url='/admin/login/')
def edit_mahasiswa(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)

    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mhs)
        if form.is_valid():
            form.save()
            return redirect('daftar_mahasiswa')
    else:
        form = MahasiswaForm(instance=mhs)

    return render(request, 'mahasiswa/input.html', {
        'form': form,
        'edit_mode': True,
        'mahasiswa_id': id,
    })


def daftar_mahasiswa(request):
    semua_mahasiswa = Mahasiswa.objects.all().order_by('id')
    total = semua_mahasiswa.count()
    whatsapp_count = Mahasiswa.objects.exclude(whatsapp='').count()
    alamat_count = Mahasiswa.objects.exclude(alamat='').count()
    return render(request, 'mahasiswa/list.html', {
        'semua_mahasiswa': semua_mahasiswa,
        'total_mahasiswa': total,
        'whatsapp_count': whatsapp_count,
        'alamat_count': alamat_count,
    })


# ✅ Fungsi ekspor ke Excel
def export_excel(request):
    # Buat workbook dan worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Data Mahasiswa"

    # Header kolom
    headers = ["No", "Nama", "NPM", "Email", "WhatsApp"]
    sheet.append(headers)

    # Isi data dari database
    for i, mhs in enumerate(Mahasiswa.objects.all().order_by('id'), start=1):
        sheet.append([i, mhs.nama, mhs.npm, mhs.email, mhs.whatsapp])

    # Gaya header
    for cell in sheet[1]:
        cell.font = openpyxl.styles.Font(bold=True, color="FFFFFF")
        cell.fill = openpyxl.styles.PatternFill(start_color="00B0F0", end_color="00B0F0", fill_type="solid")

    # Atur lebar kolom otomatis
    for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column].width = adjusted_width

    # Siapkan respons download
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = 'attachment; filename="data_mahasiswa.xlsx"'
    workbook.save(response)
    return response
