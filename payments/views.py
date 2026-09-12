from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics

from payments.models import Payment
from payments.serializers import PaymentSerializer


def health_check(request):
    """
    Health check endpoint to verify the application's status.
    Returns a JSON response indicating the application is running.
    """
    return JsonResponse({
            "status": "healthy",
            "service": "payflow-api",
        }
    )

class PaymentCreateView(generics.CreateAPIView):
    """
    API view to handle the creation of Payment instances.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
	
