from decimal import Decimal

import pytest
from payments.models import Payment

@pytest.mark.django_db
def test_payment_is_created_with_pending_status():
    payment = Payment.objects.create(amount=Decimal('1500.00'), currency='MXN')
    assert payment.status == Payment.Status.PENDING
    assert payment.amount == Decimal('1500.00')
    assert payment.currency == 'MXN'
    
