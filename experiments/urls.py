from django.conf.urls import url, include
from rest_framework.urlpattersn import format_suffix_patterns
from experiments import views

# Experiments URLs
urlpatterns = [
	url(r'^experiments/$', views.ExperimentList.as_view()),
	url(r'^experiments/(?P<pk>[0-9]+)/$', views.ExperimentDetail.as_view()),

]

# User URLs
urlpatterns += [
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

"""
The r'^api-auth/' part of pattern can actually be whatever URL you want to use.
Only restriction is that the included URLs must have 'rest_framework' namespace

This will add the ability to login to a browsable API.
"""

# API URLs
urlpatterns += [
	url(r'api-auth/', include('rest_framwork.urls',
				 	namespace='rest_framework'))	
]

# Create format suffixes patterns for our URLs
urlpatterns = format_suffix_patterns(urlpatterns)
