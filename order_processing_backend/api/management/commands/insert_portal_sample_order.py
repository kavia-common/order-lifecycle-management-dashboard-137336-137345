from django.core.management.base import BaseCommand
from api.models import Order


class Command(BaseCommand):
    """
    Django management command to insert a single recognizable sample order
    for the portal to display via the /api/orders/ endpoint.
    """

    help = "Insert a single sample order 'Portal Test Customer' so it's visible in the portal."

    # PUBLIC_INTERFACE
    def handle(self, *args, **options):
        """Create or update a single sample order with recognizable dummy data.

        Creates an Order with:
        - order_number: ORD-PORTAL-SAMPLE-001
        - customer_name: 'Portal Test Customer'
        - status: 'created'
        - total_amount: 123.45

        If the order already exists, it will be updated to ensure visibility.
        """
        order, created = Order.objects.update_or_create(
            order_number="ORD-PORTAL-SAMPLE-001",
            defaults={
                "customer_name": "Portal Test Customer",
                "status": Order.Status.CREATED,
                "total_amount": 123.45,
                "delivered_at": None,
                "invoiced_at": None,
            },
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created sample order: {order.order_number}"))
        else:
            self.stdout.write(self.style.WARNING(f"Updated existing sample order: {order.order_number}"))

        self.stdout.write(
            f"Order visible at /api/orders/ with status '{order.status}' and customer '{order.customer_name}'."
        )
