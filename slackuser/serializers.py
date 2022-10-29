from rest_framework import serializers
from .models import *


class SlackUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackUser
        fields = "__all__"
    