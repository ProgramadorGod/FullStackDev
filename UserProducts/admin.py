from django.contrib import admin

from UserProducts.models import ProductRelation
# Register your models here.

@admin.register(ProductRelation)
class ProductRelationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product"
    )
