from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.home, name="home_page"),
    url(r'^submit$', views.submit, name="submit_page"),
]
