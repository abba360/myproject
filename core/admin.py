from . import models
from django.contrib import admin


class ProductImagesAdmin(admin.TabularInline):
    extra, model = 0, models.ProductImages


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = [
        "user",
        "title",
        "product_image",
        "price",
        "featured",
        "product_status",
        "pid",
    ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_image"]


@admin.register(models.CartOrder)
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "price", "paid_status", "order_date", "product_status"]


@admin.register(models.CartOrderItems)
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "qty", "price"]


@admin.register(models.ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "product",
        "review",
        "rating",
    ]


@admin.register(models.Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ["user", "product"]


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "status"]


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone_no", "message"]


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin): ...


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin): ...
