from django.urls import path
from .views import (
    WargaListView, WargaDetailView, PengaduanListView, WargaCreateView, 
    PengaduanCreateView, WargaUpdateView, WargaDeleteView, landing_view,
    PengaduanUpdateView, PengaduanDeleteView
)

urlpatterns = [
    path('', landing_view, name='landing'),
    path('warga/', WargaListView.as_view(), name='warga-list'),
    path('warga/<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('warga/<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('warga/<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),
    path('warga/tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/update/', PengaduanUpdateView.as_view(), name='pengaduan-update'),
    path('pengaduan/<int:pk>/delete/', PengaduanDeleteView.as_view(), name='pengaduan-delete'),
]
