from django.conf.urls import url
from .views import index, UserCreate, MoveIn, ProductClassCreate

urlpatterns = [
    url(r'sd^$', UserCreate.as_view(), name='create-user'),
    url(r'^$', ProductClassCreate.as_view(), name='create-move-in'),

]
