from django.urls import path

from .views import health_check, PaymentCreateView


urlpatterns = [
    path("health/", health_check, name="health"),
    path("payments/", PaymentCreateView.as_view(), name="payment-create"),
]