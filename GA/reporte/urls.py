from django.conf.urls import url
from .views import (
    LandingPage, DateReportView, ProductReportView,
    LocationReportView, GeneralReportView, DisposableProductView, 
)

app_name = 'reporte'
urlpatterns = [
    url(r'^home/$', LandingPage.as_view(), name='home'),
    url(r'^disposable-product/$', DisposableProductView.as_view(), name='disposable-product'),
    url(r'^general-report/$', GeneralReportView.as_view(), name='general'),
    url(r'^date-report/$', DateReportView.as_view(), name='date'),
    url(r'^product-report/$', ProductReportView.as_view(), name='product'),
    url(r'^location-report/$', LocationReportView.as_view(), name='location'),
]
