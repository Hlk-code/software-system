from django.conf.urls import url
from resident import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
]