from django.conf.urls import url
from .views import (
    UserCreate, MoveInCreate, MoveOutView, ProductClassCreate,
    ProductClassList, LandingPage, UserCreate, PrintCodes,
    PriceUpdateView,
    DisposableProductView, Login, log_out, make_single_move_out,
    get_product_global_stock, get_product_class_details,
    get_products, get_product_stock, generate_file
)

app_name = 'inventario'
urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
    url(r'^log-out/$', log_out, name='log-out'),
    url(r'^create-user/$', UserCreate.as_view(), name='user-create'),
    url(r'^home/$', LandingPage.as_view(), name='home'),
    url(r'^product-create/$', ProductClassCreate.as_view(), name='create-product'),
    url(r'^print-product-codes/$', PrintCodes.as_view(), name='print-product-codes'),
    url(r'^product-search/$', ProductClassList.as_view(), name='product-class-search'),
    url(r'^disposable-product/$', DisposableProductView.as_view(), name='disposable-product'),
    url(r'^product-out/$', MoveOutView.as_view(), name='move-out'),
    url(r'^product-in/$', MoveInCreate.as_view(), name='move-in'),
    url(r'^product-update-price/$', PriceUpdateView.as_view(), name='product-price-update'),
    url(r'^print-product-codes/$', PrintCodes.as_view(), name='print-codes'),
    url(r'^ajax/product_class_details/$', get_product_class_details, name='get_product_class'),
    url(r'^ajax/products/$', get_products, name='get-products'),
    url(r'^ajax/single-product-out/',make_single_move_out , name='single-move-out'),
    url(r'^ajax/get_product_stock', get_product_stock, name='get_product_stock'),
    url(r'^ajax/get_product_global_stock', get_product_global_stock, name='get_product_global_stock'),
    url(r'^ajax/generate_file', generate_file, name='generate-file'),
]
