from rest_framework import serializers


class CalcSerializer(serializers.Serializer):
    x = serializers.IntegerField(label="Enter the value of X")
    y = serializers.IntegerField(label="Enter the value of Y")
    operation_type = serializers.CharField(label="Select operation type")