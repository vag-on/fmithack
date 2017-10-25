from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/$', views.login, name='login'),
	url(r'^registration/$', views.registr, name='registr'),
	url(r'^rasp/$', views.rasp, name='rasp'),
	url(r'^bj/$', views.bj, name='bj'),
	url(r'^contacts/$', views.contacts, name='contacts'),
]

