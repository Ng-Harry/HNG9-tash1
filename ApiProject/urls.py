from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from slackuser import views




router = routers.DefaultRouter()
router.register('SlackUser', views.SlackuserViewSet)

def index():
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("stagetwo/", include('stage2.urls')),
]
