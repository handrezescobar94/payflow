from django.shortcuts import render
from django.http import JsonResponse


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
	
