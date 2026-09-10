from django.db import models


class Payment(models.Model):

	class Status(models.TextChoices):
		PENDING = "PENDING", "Pending"
		PROCESSING = "PROCESSING", "Processing"
		COMPLETED = "COMPLETED", "Completed"
		FAILED = "FAILED", "Failed"
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	currency = models.CharField(max_length=3, default="MXN")
	status = models.CharField(
		max_length=20,
		choices=Status.choices,
		default=Status.PENDING,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Payment {self.id} - {self.amount} {self.currency} - {self.status}"
