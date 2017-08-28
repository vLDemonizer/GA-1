from django.conf.urls import url
from .views import UserCreate, MoveIn, ProductClassCreate, LandingPage

urlpatterns = [
    url(r'^$', LandingPage.as_view(), name='home'),
    url(r'^product-create/$', ProductClassCreate.as_view(), name='create-product'),
    url(r'^product-in/$', MoveIn.as_view(), name='move-in'),

]
