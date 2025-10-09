from django import forms
from .models import Warga, Pengaduan

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        # Tentukan field mana saja dari model yang ingin ditampilkan di form
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
        
        # Kustomisasi widget dengan neuromorphism styling
        widgets = {
            'nik': forms.TextInput(attrs={'class': 'neuro-input', 'placeholder': 'Masukkan 16 digit NIK'}),
            'nama_lengkap': forms.TextInput(attrs={'class': 'neuro-input', 'placeholder': 'Masukkan nama lengkap'}),
            'alamat': forms.Textarea(attrs={'class': 'neuro-textarea', 'rows': 3, 'placeholder': 'Masukkan alamat lengkap'}),
            'no_telepon': forms.TextInput(attrs={'class': 'neuro-input', 'placeholder': 'Contoh: 08123456789'}),
        }

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        # Tentukan field mana saja dari model yang ingin ditampilkan di form
        fields = ['pelapor', 'judul', 'deskripsi', 'status']
        
        # Kustomisasi widget dengan neuromorphism styling
        widgets = {
            'pelapor': forms.Select(attrs={'class': 'neuro-select'}),
            'judul': forms.TextInput(attrs={'class': 'neuro-input', 'placeholder': 'Masukkan judul pengaduan'}),
            'deskripsi': forms.Textarea(attrs={'class': 'neuro-textarea', 'rows': 5, 'placeholder': 'Jelaskan detail pengaduan Anda'}),
            'status': forms.Select(attrs={'class': 'neuro-select'}),
        }