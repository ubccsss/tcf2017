from django.conf.urls import patterns, url
from tcf14 import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^map/?$', views.map, name='map'),
	url(r'^map/(?P<id>\d+)/$', views.map, name='map_id'),
	url(r'^list$', views.ListView.as_view(), name='list'),
	url(r'^company/(?P<pk>\d+)/$', views.CompanyView.as_view(), name='company'),
	url(r'^booth/(?P<id>\d+)/$', views.booth, name='booth'),
)