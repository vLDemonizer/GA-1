from django.conf.urls import url
from . import views

app_name = 'rrhh'
urlpatterns = [
    url(r'^$', views.IndexRRHHView.as_view(), name='index'),
    url(r'^employee/$', views.EmployeeView.as_view(), name='employee'),
    url(r'^spouse/$', views.SpouseView.as_view(), name='spouse'),
    url(r'^spawn/$', views.SpawnView.as_view(), name='spawn'),
    url(r'^position/$', views.PositionView.as_view(), name='position'),
    url(r'^employee-control/$', views.EmployeeControlView.as_view(), name='employee-control'),
    url(r'^control-in/$', views.ControlInView.as_view(), name='control-in'),
    url(r'^control-out/$', views.ControlOutView.as_view(), name='control-out'),
]