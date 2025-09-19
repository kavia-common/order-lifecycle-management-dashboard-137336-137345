from django.db import models


class Order(models.Model):
    """
    Order model representing the lifecycle of an order in the system.
    """

    class Status(models.TextChoices):
        CREATED = "created", "Created"
        DELIVERED = "delivered", "Delivered"
        INVOICED = "invoiced", "Invoiced"

    order_number = models.CharField(max_length=64, unique=True, help_text="External facing order identifier")
    customer_name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
        help_text="Lifecycle status of the order",
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    invoiced_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.order_number} - {self.customer_name} ({self.status})"
