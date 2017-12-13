from django.conf.urls import url

from .import views

app_name = 'demo'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]