from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    modified_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

class Supplier(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

class ItemTypes(BaseModel):
    type = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=8, null=True, blank=True)

class Items(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    item_type = models.ForeignKey(ItemTypes, on_delete=models.DO_NOTHING)

class StockOut(BaseModel):
    item = models.ForeignKey(
        Items, on_delete=DO_NOTHING, null=True, blank=True
    )
    quantity = models.DecimalField(
        max_digits=19, decimal_places=4, null=True, blank=True
    )

class StockIn(BaseModel):
    item = models.ForeignKey(
        Items, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    quantity = models.DecimalField(
        max_digits=19, decimal_places=4, null=True, blank=True
    )

class Released(BaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(
        max_digits=19, decimal_places=4, null=True, blank=True
    )

class InventoryLog(BaseModel):
    stock_in = models.ForeignKey(StockIn, on_delete=models.DO_NOTHING)
    stock_out = models.ForeignKey(StockOut, on_delete=models.DO_NOTHING)
    released = models.ForeignKey(Released, on_delete=models.DO_NOTHING)