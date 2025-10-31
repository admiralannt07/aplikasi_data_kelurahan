from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        # Tentukan field dari model Warga yang ingin kita ekspos di API
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']


class PengaduanSerializer(serializers.ModelSerializer):
    # Field read-only untuk menampilkan nama pelapor tanpa nested yang ribet
    pelapor_nama = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)

    class Meta:
        model = Pengaduan
        # Ekspos field inti pengaduan + referensi pelapor
        fields = [
            'id',
            'judul',
            'deskripsi',
            'status',
            'tanggal_lapor',
            'pelapor',      # ini akan tampil sebagai ID warga (primary key)
            'pelapor_nama', # biar manusiawi, tampilkan juga nama lengkap pelapor
        ]