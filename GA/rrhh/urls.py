from django.conf.urls import url
from . import views

app_name = 'rrhh'
urlpatterns = [
    url(r'^$', views.IndexRRHHView.as_view(), name='index'),
    url(r'^employee-list/$', views.ListEmployee.as_view(), name='employee-list'),
    url(r'^employee-create/$', views.CreateEmployee.as_view(), name='employee-create'),
    url(r'^employee-update/(?P<pk>\d+)/$', views.UpdateEmployee.as_view(), name='employee-update'),
    url(r'^employee-detail/(?P<pk>\d+)/$', views.DetailEmployee.as_view(), name='employee-detail'),
    url(r'^employee-delete/(?P<pk>\d+)/$', views.DeleteEmployee.as_view(), name='employee-delete'),

    # url(r'^product-list/$', views.ListProduct.as_view(), name='product-list'),
    # url(r'^product-create/$', views.CreateProduct.as_view(), name='product-create'),
    # url(r'^product-update/(?P<pk>\d+)/$', views.UpdateProduct.as_view(), name='product-update'),
    # url(r'^product-delete/(?P<pk>\d+)/$', views.DeleteEmployee.as_view(), name='product-delete'),

    # url(r'^employee-control-list/$', 
    #     views.EmployeeControlListView.as_view(), name='employee-control-list'),
        
    # url(r'^employee-control-create/(?P<pk>\d+)/$', 
    #     views.EmployeeControlView.as_view(), name='employee-control-create'),

    # url(r'^employee-control-update/(?P<pk>\d+)/(?P<employee>\d+)/$', 
    #     views.EmployeeControlUpdateView.as_view(), name='employee-control-update'),

    # url(r'^employee-control-delete/(?P<pk>\d+)/$', 
    #     views.EmployeeControlDeleteView.as_view(), name='employee-control-delete'),
]