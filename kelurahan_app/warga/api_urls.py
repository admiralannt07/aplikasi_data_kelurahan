from django.urls import path
from .views import WargaListAPIView, WargaRetrieveAPIView

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaRetrieveAPIView.as_view(), name='api-warga-detail'),
]