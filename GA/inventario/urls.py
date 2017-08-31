from django.conf.urls import url
from .views import (
    UserCreate, MoveInCreate, MoveOutView, ProductClassCreate,
    LandingPage, UserCreate, Login, log_out,
    get_product_class_details, get_products
)

urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
    url(r'^log-out/$', log_out, name='log-out'),
    url(r'^create-user/$', UserCreate.as_view(), name='user-create'),
    url(r'^home/$', LandingPage.as_view(), name='home'),
    url(r'^product-create/$', ProductClassCreate.as_view(), name='create-product'),
    url(r'^product-out/$', MoveOutView.as_view(), name='move-out'),
    url(r'^product-in/$', MoveInCreate.as_view(), name='move-in'),
    url(r'^ajax/product_class_details/$', get_product_class_details, name='get_product_class'),
    url(r'^ajax/products/$', get_products, name='get_products'),




]
