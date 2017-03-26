from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registration$', views.registration),
    url(r'^create_user$', views.createuser),
    url(r'^login', views.login_page),
    url(r'^log', views.log),

]
