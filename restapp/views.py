from django.shortcuts import render,get_list_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from restapp.models import Employee
from restapp.serializers import Employee_serializer

# Create a class based  views
class Employeelist(APIView):
    def get(self,request):
        lst=get_list_or_404(Employee)
        slst=Employee_serializer(lst,many=True)
        return Response(slst.data)

    def post(self,request):
        sobj=Employee_serializer(data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data)
            status=status.HTTP_201_CREATED
        else:
            return status.HTTP_400_BAD_REQUEST
