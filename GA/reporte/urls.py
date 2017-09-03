from django.conf.urls import url
from .views import ( LandingPage,

)

app_name = 'reporte'
urlpatterns = [
    url(r'^home/$', LandingPage.as_view(), name='home'),
]
