from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class SlackuserViewSet(viewsets.ModelViewSet):
    queryset = SlackUser.objects.all()
    serializer_class = SlackUserSerializer
