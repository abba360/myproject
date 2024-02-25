from . import views
from django.urls import path

app_name = "core"
urlpatterns = [
    # Homepage
    path("",views.index, name='index'),
    path("contact",views.contact_view, name='contact'),
    path("aboutus/",views.about_us_view, name='aboutus'),
    path("checkout/",views.checkout_view, name='checkout'),
    path("products/",views.get_product_list_view, name='products-list'),
    path("single_product/<pid>/",views.single_product_view, name='single_product'),

    path('cart/', views.view_cart, name='view_cart'),
    path("search/",views.search_view, name='search'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path("product-list/", views.category_view, name="category-all"),
    path("product-list/<name>/", views.category_view, name="category-one"),
]
    # path("products/",views.get_product_list_view, name='products-list'),
    # path("products/",views.get_product_list_view, name='products-list'),
    # path("products/",views.get_product_list_view, name='products-list'),
    # path("products/",views.get_product_list_view, name='products-list'),
    # path("products/",views.get_product_list_view, name='products-list'),
    




