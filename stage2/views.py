from . serializers import *
from . models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class CalcApiView(APIView):
    serializer_class=CalcSerializer
    
    def post(self,request):
        print("Request data is :", request.data)
        serializer_obj = CalcSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            if serializer_obj.data.get("operation_type") == "addition":
                x = serializer_obj.data.get("x")
                y = serializer_obj.data.get("y")
                result = x + y
                slackUsername = "NgHarry"
                return Response({"slackUsername": slackUsername,"result":result})
            
            elif serializer_obj.data.get("operation_type") == "subtration":
                x = serializer_obj.data.get("x")
                y = serializer_obj.data.get("y")
                result = x - y
                slackUsername = "NgHarry"
                return Response({"slackUsername": slackUsername,"result":result})
            
            elif serializer_obj.data.get("operation_type") == "multiplication":
                x = serializer_obj.data.get("x")
                y = serializer_obj.data.get("y")
                result = x * y
                slackUsername = "NgHarry"
                return Response({"slackUsername": slackUsername,"result":result})
            
            else:
                message = "Please select a valid operator type!!!"
                return Response({"message": message})
            Calc.objects.create(x=serializer_obj.data.get('x'), y=serializer_obj.data.get('y'), operation_type=serializer_obj.data.get('operation_type'))
            cal = Calc.objects.all().filter(id=request.data.get("id"))
        return Response({"message":"message is here", "cal":cal})