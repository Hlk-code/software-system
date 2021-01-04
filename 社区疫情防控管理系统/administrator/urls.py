from administrator import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.manage,name='manage'),
]