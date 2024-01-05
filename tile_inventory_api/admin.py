from django.contrib import admin
from .models import (
    Tile,
    Warehouse,
    Inventory
)

# Register your models here.
admin.site.register(Tile)
admin.site.register(Warehouse)
admin.site.register(Inventory)