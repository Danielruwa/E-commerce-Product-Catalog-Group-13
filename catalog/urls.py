from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet

def health_check(request):
    return JsonResponse({"status": "ok"})

# Create the router and register the viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)

urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("", include(router.urls)),   # add the router endpoints
]

