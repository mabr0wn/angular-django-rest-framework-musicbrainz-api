from django.conf.urls import url, include
from rest_framework.urlpattersn import format_suffix_patterns
from experiments import views

# API endpoints
# Create format suffixes patterns for our URLs
urlpatterns = format_suffix_patterns([
	url(r'^$', views.api_root),
	url(r'^experiments/$', views.ExperimentList.as_view(), name='experiment-list'),
	url(r'^experiments/(?P<pk>[0-9]+)/$', views.ExperimentDetail.as_view(), name='experiment-detail'),
	url(r'^experiments/(?P<pk>[0-9]+)/hightlight/$', views.ExperimentHighlight.as_view(), name='experiment-highlight'),
	url(r'users/$', views.UserList.as_view(), name='user-list'),
	url(r'users/(?P<pk>[0-9]+)/', views.UserDetail.as_view(), name='user-detail'),
])


"""
The r'^api-auth/' part of pattern can actually be whatever URL you want to use.
Only restriction is that the included URLs must have 'rest_framework' namespace

This will add the ability to login to a browsable API.
"""

# Login and Logout views for the browsable API.
urlpatterns += [
	url(r'api-auth/', include('rest_framwork.urls',
				 	namespace='rest_framework'))	
]

