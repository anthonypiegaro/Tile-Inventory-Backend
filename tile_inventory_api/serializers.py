from rest_framework import serializers
from .models import (
    Tile,
    Warehouse,
    Inventory
)


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ['id', 'name']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["name", "location"]


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["tile", "warehouse", "quantity"]


class InventorySpecificSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Inventory
        fields = ["name", "quantity"]
    
    def get_name(self, obj):
        return obj.warehouse.name


class TileWithInventorySerializer(serializers.ModelSerializer):
    inventory = serializers.SerializerMethodField()

    class Meta:
        model = Tile
        fields  = ("id", "name", "inventory")
    
    def get_inventory(self, obj):
        inventory_items = Inventory.objects.filter(tile=obj)
        return InventorySpecificSerializer(inventory_items, many=True).data