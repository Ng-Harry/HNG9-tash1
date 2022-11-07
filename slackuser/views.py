from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt 
def index(request):
    if request.method == "POST":
        data = request.POST
        operation_type = data.get("operation_type")
        x: int = int(data.get("x"))
        y: int = int(data.get("y"))
        
        response = {
            
        }

        if (operation_type.lower() == "addition") | ("add" in operation_type.lower()):
            result = x + y
            operation_type = "addition"
        elif (operation_type.lower() == "subtraction") | ("subtract" in operation_type.lower()):
            result = x - y
            operation_type = "subtraction"
        elif (operation_type.lower() == "multiplication") | ("multiply" in operation_type.lower()):
            result = x * y
            operation_type = "multiplication"

    response={
        "slackUsername": "topefolorunso",
        "result": result,
        "operation_type": operation_type,
    }

    return HttpResponse(json.dumps(response), content_type='application/json')


class SlackuserViewSet(viewsets.ModelViewSet):
    queryset = SlackUser.objects.all()
    serializer_class = SlackUserSerializer

    

