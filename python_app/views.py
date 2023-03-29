import datetime
from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime
from django.shortcuts import render,get_object_or_404
from . models import conn
from rest_framework.views import APIView
from . serializers import serial
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def now(request):
    date = datetime.datetime.now()
    msg = f"Hey today date is {date}"
    return HttpResponse(msg)
def hello(request):
    return render(request, 'hello.html',{'name':'Bala Krishan baddi'})

class connection(APIView):
   def get_object(self, pk):
            try:
                return conn.objects.get(pk=pk)
            except conn.DoesNotExist:
                raise Http404
   def get(self, request, pk=None, format=None):

        if pk:
                data = self.get_object(pk)
                var_serializer = serial(data)
                return Response([var_serializer.data])

        else:
                data = conn.objects.all()
                var_serializer = serial(data, many=True)

                return Response(var_serializer.data)

   def post(self, request, format=None):
       data = request.data
       var_serializer = serial(data=data)

       var_serializer.is_valid(raise_exception=True)

       var_serializer.save()

       response = Response()

       response.data = {
           'message': 'connect Created Successfully',
           'data': var_serializer.data
       }
       return response