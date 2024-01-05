from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Tile,
    Warehouse,
    Inventory
)
from .serializers import (
    TileSerializer,
    WarehouseSerializer,
    InventorySerializer,
    TileWithInventorySerializer
)


class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer
    permission_classes = [IsAuthenticated]


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]


class TileWithInventoryList(generics.ListAPIView):
    queryset = Tile.objects.all()
    serializer_class = TileWithInventorySerializer
    permission_classes = [IsAuthenticated]