from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^detail/(?P<item_id>[0-9]+)/$', views.detail, name='question'),
  url(r'^logout/$',views.logout_view, name='logout'),
  url(r'^Collection/$', views.collection, name='collection'),
  url(r'^Contact/$',views.contact, name='contact'),
  url(r'^About/$', views.about, name='about'),
  url(r'^Payment/$', views.payment, name='payment'),
  url(r'^Create/$', views.createItem, name='create'),
  url(r'^Account/(?P<user>[a-zA-Z0-9]+)/$', views.account,name='account'),
]
