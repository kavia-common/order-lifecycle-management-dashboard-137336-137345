from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import Order


class Command(BaseCommand):
    help = "Seed the database with one order in each key state: created, delivered, invoiced."

    # PUBLIC_INTERFACE
    def handle(self, *args, **options):
        """
        Create or update three orders ensuring one exists for each key status.
        """
        now = timezone.now()

        # Created
        created_order, _ = Order.objects.update_or_create(
            order_number="ORD-CREATED-001",
            defaults={
                "customer_name": "Alice Anderson",
                "status": Order.Status.CREATED,
                "total_amount": 125.50,
                "delivered_at": None,
                "invoiced_at": None,
            },
        )

        # Delivered
        delivered_order, _ = Order.objects.update_or_create(
            order_number="ORD-DELIVERED-001",
            defaults={
                "customer_name": "Bob Brown",
                "status": Order.Status.DELIVERED,
                "total_amount": 250.00,
                "delivered_at": now,
                "invoiced_at": None,
            },
        )

        # Invoiced
        invoiced_order, _ = Order.objects.update_or_create(
            order_number="ORD-INVOICED-001",
            defaults={
                "customer_name": "Carla Carter",
                "status": Order.Status.INVOICED,
                "total_amount": 399.99,
                "delivered_at": now,
                "invoiced_at": now,
            },
        )

        self.stdout.write(self.style.SUCCESS("Seeded sample orders:"))
        self.stdout.write(f" - {created_order.order_number} [{created_order.status}]")
        self.stdout.write(f" - {delivered_order.order_number} [{delivered_order.status}]")
        self.stdout.write(f" - {invoiced_order.order_number} [{invoiced_order.status}]")
