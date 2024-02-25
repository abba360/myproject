from django.db import models
from userauths.models import User
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField


# Create your models here.

STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("Delivered", "Delivered"),
)

PRODUCT_CHOICE = (
    ("small", "Small"),
    ("medium", "Medium"),
    ("large", "Large"),
    ("extra_large", "Extra Large"),
)

STATUS = (
    ("draft", "Draft"),
    ("deliver", "Delivered"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Category(models.Model):
    cid = ShortUUIDField(
        unique=True,
        length=10,
        max_length=20,
        prefix="cat_",
        alphabet="abcdefg1234",
    )
    title = models.CharField(max_length=100, default="Fresh Vege product.")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" hight="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Tags(models.Model):
    pass


class Product(models.Model):
    pid = ShortUUIDField(
        unique=True,
        length=10,
        max_length=20,
        prefix="prd_",
        alphabet="abcdefg1234",
    )
    # slug = models.SlugField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100, default="Fresh product.")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is a product.")

    price = models.DecimalField(max_digits=9999999, decimal_places=2, default="20")
    old_price = models.DecimalField(max_digits=9999999, decimal_places=2, default="20")

    specifications = models.TextField(
        null=True,
        blank=True,
    )
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    product_status = models.CharField(
        choices=STATUS, max_length=10, default="In Review"
    )
    # product_choice = models.CharField(choices=STATUS, max_length=10, default="In Review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    stock_count = models.CharField(
        choices=STATUS, max_length=10, default="10", blank=True
    )
    life = models.CharField(max_length=100, default="2 days", blank=True)
    sku = ShortUUIDField(
        unique=True,
        length=4,
        max_length=10,
        prefix="sku_",
        alphabet="1234567890",
    )

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def product_image(self):
        return mark_safe('<img src="%s" width="50" hight="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price


class ProductImages(models.Model):
    image = models.ImageField(upload_to="product-image.jpg", default="product.jpg")
    product = models.ForeignKey(
        Product,
        related_name="p_image",
        max_length=100,
        on_delete=models.SET_NULL,
        null=True,
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price


###################################################### Cart, OrderItemms #########################################################
###################################################### Cart, OrderItemms #########################################################
###################################################### Cart, OrderItemms #########################################################
###################################################### Cart, OrderItemms #########################################################


class CartOrder(models.Model):
    user = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=9999999, decimal_places=2, default="20")
    paid_status = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(
        choices=STATUS_CHOICE, max_length=30, default="Processing"
    )

    class Meta:
        verbose_name_plural = "Cart Orders"


class CartOrderItems(models.Model):
    qty = models.IntegerField(default=0)
    order = models.ForeignKey(CartOrder, models.CASCADE)
    product = models.ForeignKey(Product, models.PROTECT)
    price = models.DecimalField(max_digits=9999999, decimal_places=2, default="20")

    def order_image(self):
        return mark_safe('<img src="/media/%s" width="50" hight="50" />' % (self.image))

    class Meta:
        verbose_name_plural = "Cart Order Items"


###################################################### ProductReview, Whishlist and Address #########################################################
###################################################### ProductReview, Whishlist and Address #########################################################
###################################################### ProductReview, Whishlist and Address #########################################################
###################################################### ProductReview, Whishlist and Address #########################################################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title

    def rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return self.product.title


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return self.Address.address


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_no = models.CharField(max_length=15)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Contact Us"


class Cart(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
