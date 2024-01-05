from django.db import models

class Tile(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, related_name="inventories")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tile.name} in {self.warehouse.name}"

    class Meta:
        unique_together = ('tile', 'warehouse')  # Ensures the combination of tile and warehouse is unique
