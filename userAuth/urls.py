from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.logins, name="login_page"),
    url(r'^signup$', views.signup, name="signup_page")
]