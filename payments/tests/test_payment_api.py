from decimal import Decimal

import pytest
from rest_framework.test import APIClient

from payments.models import Payment


@pytest.mark.django_db
def test_create_payment():
    client = APIClient()

    response = client.post(
        "/api/payments/",
        {
            "amount": "1499.99",
            "currency": "MXN",
        },
        format="json",
    )

    assert response.status_code == 201

    payment = Payment.objects.get()

    assert payment.amount == Decimal("1499.99")
    assert payment.currency == "MXN"
    assert payment.status == Payment.Status.PENDING

    assert response.data["id"] == payment.id
    assert response.data["status"] == Payment.Status.PENDING