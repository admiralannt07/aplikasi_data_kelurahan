from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from django.urls import reverse_lazy
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer


# Create your views here.
def landing_view(request):
    """
    View untuk halaman landing dengan statistik kelurahan
    """
    context = {
        'total_warga': Warga.objects.count(),
        'total_pengaduan': Pengaduan.objects.count(),
        'pengaduan_selesai': Pengaduan.objects.filter(status='SELESAI').count(),
        'pengaduan_proses': Pengaduan.objects.filter(status='DIPROSES').count(),
    }
    return render(request, 'warga/landing.html', context)

class WargaListView(ListView):
    model = Warga
    # Django secara otomatis akan mencari template di:
    # <nama_app>/<nama_model>_list.html -> warga/warga_list.html

class WargaDetailView(DetailView):
    model = Warga
    # Django secara otomatis akan mencari template di:
    # <nama_app>/<nama_model>_detail.html -> warga/warga_detail.html

class PengaduanListView(ListView):
    model = Pengaduan
    # Django secara otomatis akan mencari template di:
    # <nama_app>/<nama_model>_list.html -> warga/pengaduan_list.html
    
    def get_context_data(self, **kwargs):
        """
        Menambahkan statistik pengaduan ke context untuk efisiensi query
        """
        context = super().get_context_data(**kwargs)
        
        # Hitung statistik dengan query yang efisien
        context['total_pengaduan'] = self.get_queryset().count()
        context['pengaduan_baru'] = self.get_queryset().filter(status='BARU').count()
        context['pengaduan_diproses'] = self.get_queryset().filter(status='DIPROSES').count()
        context['pengaduan_selesai'] = self.get_queryset().filter(status='SELESAI').count()
        
        return context

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list') # Arahkan ke daftar warga setelah sukses

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list') # Arahkan ke daftar pengaduan setelah sukses
    
class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' # Kita pakai template yang sama
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    """
    View untuk mengupdate data pengaduan
    """
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html' # Menggunakan template yang sama dengan create
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    """
    View untuk menghapus data pengaduan
    """
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

# --- API VIEWS ---
class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaRetrieveAPIView(RetrieveAPIView):
    """
    API untuk mengambil detail satu Warga berdasarkan primary key (ID).
    Contoh: /api/warga/1/
    """
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer