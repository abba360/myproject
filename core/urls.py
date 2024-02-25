from django.urls import path

from core.views import index, checkout_view, get_product_list_view, aboutus_view, single_product_view, contact_view, search_view, view_cart,add_to_cart, remove_from_cart
app_name = "core"


urlpatterns = [
    # Homepage
    path("",index, name='index'),
    path("products/",get_product_list_view, name='products-list'),
    path("aboutus/",aboutus_view, name='aboutus'),
    path("contact",contact_view, name='contact'),
    path("checkout/",checkout_view, name='checkout'),
    path("single_product/<pid>/",single_product_view, name='single_product'),

    path("search/",search_view, name='search'),
    path('cart/', view_cart, name='view_cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
    # path("products/",get_product_list_view, name='products-list'),
    # path("products/",get_product_list_view, name='products-list'),
    # path("products/",get_product_list_view, name='products-list'),
    # path("products/",get_product_list_view, name='products-list'),
    # path("products/",get_product_list_view, name='products-list'),
    




