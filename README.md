# Aplikasi Data Kelurahan (WIP)

Proyek ini adalah aplikasi pengelolaan data kelurahan berbasis Django, dengan antarmuka web dan API sederhana menggunakan Django REST Framework (DRF). Status saat ini: masih dalam tahap pengembangan (Work In Progress).

Tujuan utama aplikasi:
- Mengelola data Warga (buat, baca, ubah, hapus) melalui antarmuka web.
- Mengelola Pengaduan yang dilaporkan oleh Warga.
- Menyediakan API untuk konsumsi data oleh aplikasi lain.

## Fitur yang tersedia
- Halaman landing dengan ringkasan statistik (jumlah warga, pengaduan, dll).
- Manajemen Warga:
  - List: /warga/
  - Detail: /warga/<id>/
  - Tambah: /warga/tambah/
  - Edit: /warga/<id>/edit/
  - Hapus: /warga/<id>/hapus/
- Manajemen Pengaduan:
  - List: /pengaduan/
  - Tambah: /pengaduan/tambah/
  - Update: /pengaduan/<id>/update/
  - Delete: /pengaduan/<id>/delete/
- API (DRF):
  - GET /api/warga/ — menampilkan daftar warga
  - GET /api/warga/<id>/ — menampilkan detail satu warga berdasarkan ID

## Teknologi yang digunakan
- Python, Django
- Django REST Framework (DRF)
- SQLite (default)

## Struktur proyek (ringkas)
- kelurahan_app/
  - manage.py
  - kelurahan_app/ (config project)
  - warga/ (aplikasi utama)
  - requirements.txt
- myenv/ (opsional, virtual environment)

## Persyaratan
- Python 3.x (direkomendasikan menggunakan virtual environment)

## Cara menjalankan secara lokal (Windows/Powershell)
1. (Opsional) Buat dan aktifkan virtual environment
   - python -m venv myenv
   - .\myenv\Scripts\Activate.ps1
2. Masuk ke direktori project Django
   - cd kelurahan_app
3. Instal dependensi
   - pip install -r requirements.txt
4. Jalankan migrasi database
   - python manage.py migrate
5. (Opsional) Buat superuser untuk akses admin
   - python manage.py createsuperuser
6. Jalankan server pengembangan
   - python manage.py runserver

## Akses
- Antarmuka web:
  - http://localhost:8000/warga/
  - http://localhost:8000/pengaduan/
- Admin Django:
  - http://localhost:8000/admin/
- API:
  - Daftar warga: http://localhost:8000/api/warga/
  - Detail warga: http://localhost:8000/api/warga/1/

Contoh respons API (Warga):
{
  "id": 1,
  "nik": "1234567890123456",
  "nama_lengkap": "Nama Warga",
  "alamat": "Alamat Warga",
  "no_telepon": "081234567890"
}

## Status dan rencana (WIP/TODO)
- Tambahkan autentikasi/otorisasi untuk endpoint API.
- Pagination, pencarian, dan filtering pada daftar Warga/Pengaduan.
- Validasi NIK yang lebih kuat dan penanganan error yang rapi di API.
- Dokumentasi API (contoh: drf-spectacular atau drf-yasg).
- Unit test dan integration test.
- Deployment guide.

## Kontribusi
Kontribusi sangat disambut. Silakan buat pull request atau ajukan issue dengan deskripsi yang jelas.

## Lisensi
Belum ditentukan. Gunakan untuk kebutuhan belajar/pengembangan sementara.