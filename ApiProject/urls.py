from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from slackuser import views



router = routers.DefaultRouter()
router.register('SlackUser', views.SlackuserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
