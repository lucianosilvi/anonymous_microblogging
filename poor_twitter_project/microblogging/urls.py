from django.conf.urls import include, url
from rest_framework import routers
from . import views

# Django Rest Routers
router = routers.DefaultRouter()
router.register(r'tweets', views.TweetViewSet)

urlpatterns = [
    url('^save/?$', views.save_tweet, name="save_tweet"),
    url(r'^$', views.index, name="index"),
    url(r'', include(router.urls)),
]
