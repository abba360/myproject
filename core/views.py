from core import models
from django.db.models import Q
from googletrans import Translator
from django.shortcuts import render, get_object_or_404, redirect


translator = Translator()


def index(request):
    products = models.Product.objects.all()

    context = {"products": products}
    return render(request, "core/index.html", context)


def about_us_view(request):
    return render(request, "core/aboutus.html")


def checkout_view(request):
    return render(request, "core/checkout.html")


def get_product_list_view(request):
    categories = models.Category.objects.all()
    products = models.Product.objects.filter(product_status="published")

    context = {"products": products, "categories": categories}
    return render(request, "core/shop.html", context)


def single_product_view(request, pid):
    product = get_object_or_404(models.Product, pid=pid)

    context = {"product": product}
    return render(request, "core/product-single.html", context)


# cart items
def view_cart(request):
    delivery = float(55.00)
    discount = float(32.00)
    cart_items = request.user.cart.cartitem_set.all()
    sub_total = sum(item.product.price * item.quantity for item in cart_items)

    for item in cart_items:
        item.total = item.product.price * item.quantity

    total = float(sub_total) + delivery - discount
    context = {
        "total": total,
        "delivery": delivery,
        "discount": discount,
        "sub_total": sub_total,
        "cart_items": cart_items,
    }
    return render(request, "core/cart.html", context)


def add_to_cart(request, product_id):
    if request.method == "POST":
        attr = {"user": request.user}
        amount = int(request.POST.get("amount", 1))

        product = models.Product.objects.get(id=product_id)
        cart, _ = models.Cart.objects.get_or_create(**attr, defaults=attr)

        cart_item = cart.cartitem_set.filter(product=product).first()

        if cart_item:
            cart_item.quantity += amount
            cart_item.save()
        else:
            models.CartItem.objects.create(cart=cart, quantity=amount, product=product)

    return redirect(request.META.get("HTTP_REFERER"))


def remove_from_cart(request, item_id):
    if request.method == "POST":
        cart_item = models.CartItem.objects.filter(id=item_id).first()

        if cart_item:
            cart_item.delete()
    return redirect(request.META.get("HTTP_REFERER"))


def contact_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        message = request.POST["message"]
        phone_no = request.POST["phone_no"]
        full_name = request.POST["full_name"]
        models.ContactUs.objects.create(
            full_name=full_name, email=email, phone_no=phone_no, message=message
        )

        return render(request, "core/contact.html", {"full_name": full_name})
    else:
        return render(request, "core/contact.html", {})


def search_view(request):
    query = request.GET.get("q")
    products = models.Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    context = {"products": products, "query": query}
    return render(request, "core/search.html", context)


# logic


def checkout_order(request):
    # first create an order
    order = models.CartOrder.objects.create(user=request.user)

    # get all the cart items
    cart_items = request.user.cart.cartitem_set.all()

    # replicate the cart items to order items and delete them from the cart
    for item in cart_items:
        models.CartOrderItems.objects.create(
            order=order, product=item, qty=item.quantity, price=item.product.price
        )
        item.delete()

    return redirect("core:index")
