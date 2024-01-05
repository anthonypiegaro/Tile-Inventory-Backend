from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TileViewSet,
    WarehouseViewSet,
    InventoryViewSet,
    TileWithInventoryList
)

router = DefaultRouter()
router.register(r"tiles", TileViewSet)
router.register(r"warehouse", WarehouseViewSet)
router.register(r"inventory", InventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("tiles-with-inventory/", TileWithInventoryList.as_view(), name="tile-inventory-list"),
]