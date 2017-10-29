from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.logins, name="login_page"),
    url(r'^signup$', views.signup, name="signup_page"),
    url(r'^logout$', views.logouts, name="logout_page"),
]