from django.urls import path

from .views import PaymentDetailView, PaymentListCreateView, health_check


urlpatterns = [
    path("health/", health_check, name="health"),
    path("payments/", PaymentListCreateView.as_view(), name="payment-list-create"),
    path("payments/<int:pk>/", PaymentDetailView.as_view(), name="payment-detail"),
]