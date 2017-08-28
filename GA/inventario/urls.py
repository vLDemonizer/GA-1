from django.conf.urls import url
from .views import (
    UserCreate, MoveIn, ProductClassCreate,
    LandingPage, UserCreate,
    get_product_class_details, get_products
)

urlpatterns = [
    url(r'^$', UserCreate.as_view(), name='user-create'),
    url(r'^home/$', LandingPage.as_view(), name='home'),
    url(r'^product-create/$', ProductClassCreate.as_view(), name='create-product'),
    url(r'^product-in/$', MoveIn.as_view(), name='move-in'),
    url(r'^ajax/product_class_details/$', get_product_class_details, name='get_product_class'),
    url(r'^ajax/products/$', get_products, name='get_products'),




]
