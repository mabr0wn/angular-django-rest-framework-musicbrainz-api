from django.conf.urls import url
from experiments import views

urlpatterns = [
	url(r'^experiments/$', views.ExperimentList.as_view()),
	url(r'^experiments/(?P<pk>[0-9]+)/$', views.ExperimentDetail.as_view()),

]
