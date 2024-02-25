from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.models import Address, Product, ProductImages, ProductReview, CartItem, CartOrder, CartOrderItems, Category, Tags, Wishlist, ContactUs
from django.db.models import Q
from django.views.generic import ListView, DetailView, View
import googletrans
from googletrans import Translator


translator = Translator()
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request,'core/index.html',context)

def checkout_view(request):
    return render(request,'core/checkout.html')

def get_product_list_view(request):
    products = Product.objects.filter(product_status='published')
    context = {
        "products":products
    }
    return render(request,'core/shop.html',context)

def aboutus_view(request):
    context = {
    }
    return render(request,'core/aboutus.html',context)


def single_product_view(request, pid):
    product = get_object_or_404(Product,pid=pid)
    p_image = product.p_image.all()
    context = {
        "product":product,
        "p_images":p_image,
    }
    return render(request,'core/product-single.html',context)


# cart items
def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'core/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart_item, created = CartItem.objects.get_or_create(product=product, 
													user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect('core:view_cart')

def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('core:view_cart')


def contact_view(request): 
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        message = request.POST['message' ]
        new_mail = ContactUs(full_name=full_name, email=email, phone_no=phone_no, message=message)
        new_mail.save_base()
        return render(request,'core/contact.html',{"full_name":full_name})
    else:
        return render(request,'core/contact.html',{})

def search_view(request):
    query = request.GET.get("q")
   
    products = Product.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
    context = {
        "products":products,
        "query":query,
    }
    return render(request,'core/search.html',context)
