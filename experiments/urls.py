from django.conf.urls import url
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
