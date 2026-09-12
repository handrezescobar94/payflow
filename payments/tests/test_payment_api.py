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

@pytest.mark.django_db
def test_list_payments():
    Payment.objects.create(
        amount=Decimal("100.00"),
        currency="MXN",
    )
    Payment.objects.create(
        amount=Decimal("250.00"),
        currency="USD",
    )

    client = APIClient()

    response = client.get("/api/payments/")

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["amount"] == "100.00"
    assert response.data[1]["amount"] == "250.00"


@pytest.mark.django_db
def test_retrieve_payment():
    payment = Payment.objects.create(
        amount=Decimal("999.99"),
        currency="MXN",
    )

    client = APIClient()

    response = client.get(f"/api/payments/{payment.id}/")

    assert response.status_code == 200
    assert response.data["id"] == payment.id
    assert response.data["amount"] == "999.99"
    assert response.data["currency"] == "MXN"
    assert response.data["status"] == Payment.Status.PENDING