from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    url(r'$^', views.index),
    url(r'edit/(?P<id>\d+)$', views.edit),
    url(r'update/(?P<id>\d+)$', views.update),
    url(r'add/$', views.create),
    url(r'create/$', TemplateView.as_view(template_name='create_page.html')),
    url(r'update/$', views.to_update),
    url(r'delete/$', views.to_delete),
    url(r'delete/(?P<id>\d+)$', views.delete)
]