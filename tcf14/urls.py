from django.conf.urls import patterns, url, include
from django.shortcuts import redirect
from tcf14 import views

urlpatterns = patterns('',
	url(r'^mobile$', include(patterns('',
		# Map
		url(r'^map/?$', views.map, name='map'),
		url(r'^map/(?P<id>\d+)/$', views.map, name='map_id'),

		# Company Info
		url(r'^list$', views.ListView.as_view(), name='list'),
		url(r'^company/(?P<pk>\d+)/$', views.CompanyView.as_view(), name='company'),
		url(r'^booth/(?P<id>\d+)/$', views.booth, name='booth'),
		url(r'^checkin/(?P<id>\d+)/$', views.checkin, name='checkin'),

		#Static
		url(r'^$', views.index, name='index'),
		url(r'^privacy$', views.privacy, name='privacy'),
		url(r'^help$', views.help, name='help'),
		))),
	url(r'^$', redirect('index')),
	)