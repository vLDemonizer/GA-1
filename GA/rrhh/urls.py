from django.conf.urls import url
from . import views

app_name = 'rrhh'
urlpatterns = [
    url(r'^$', views.IndexRRHHView.as_view(), name='index'),
    
]