from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as drf_status
from rest_framework.request import Request
from .models import Order
from .serializers import OrderSerializer


@api_view(['GET'])
def health(request: Request):
    """
    Simple health check endpoint.
    Returns a JSON payload indicating the server is up.
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
@api_view(["GET"])
def list_orders(request: Request):
    """
    Retrieve a list of orders, optionally filtered by status.

    Query Parameters:
    - status (optional): One of ["created", "delivered", "invoiced"] to filter orders by lifecycle status.

    Returns:
    - 200 OK with a JSON array of Order objects.
    - 400 Bad Request if status filter is invalid.
    """
    status_filter = request.query_params.get("status")
    qs = Order.objects.all()
    if status_filter:
        valid_statuses = {choice for choice, _ in Order.Status.choices}
        if status_filter not in valid_statuses:
            return Response(
                {"detail": f"Invalid status '{status_filter}'. Valid: {sorted(valid_statuses)}"},
                status=drf_status.HTTP_400_BAD_REQUEST,
            )
        qs = qs.filter(status=status_filter).order_by("-created_at")
    else:
        qs = qs.order_by("-created_at")

    data = OrderSerializer(qs, many=True).data
    return Response(data, status=drf_status.HTTP_200_OK)
