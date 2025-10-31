from django.urls import path
from .views import (
    WargaListAPIView,
    WargaRetrieveAPIView,
    PengaduanListAPIView,
    PengaduanRetrieveAPIView,
)

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaRetrieveAPIView.as_view(), name='api-warga-detail'),
    path('pengaduan/', PengaduanListAPIView.as_view(), name='api-pengaduan-list'),
    path('pengaduan/<int:pk>/', PengaduanRetrieveAPIView.as_view(), name='api-pengaduan-detail'),
]