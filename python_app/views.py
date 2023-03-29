from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import conn
from rest_framework.views import APIView
from .serializers import serial
from rest_framework.response import Response
import datetime

#this will call the date
def now(request):
    return HttpResponse(f'Hai Today date is {datetime.datetime.now()}')

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

#creating the APT View for the CRUD Operations...
class connection(APIView):
    def get_object(self, pk):
        try:
            return conn.objects.get(pk=pk)
        except conn.DoesNotExist:
            raise Http404

    #get operation
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            var_serializer = serial(data)
            return Response([var_serializer.data])


        else:
            data = conn.objects.all()
            var_serializer = serial(data, many=True)
            return Response(var_serializer.data)

    #delete operation...

    # post operation updated
    def post(self, request, format=None):
        data = request.data
        var_ser = serial(data=data)
        var_ser.is_valid(raise_exception=True)

        # saving the data
        var_ser.save()
        response = Response()
        # giving response
        response.data = {
            'message': "connection created successfully",
            'date': var_ser.data
        }
        return response

    #delete operation
    def delete(self,request,pk,format=None):
        to_delete_list = conn.objects.get(pk=pk)
        to_delete_list.delete()

        return Response({
            'message':"deleted sucessfully"
        })

    # put operation...
    def put(self, request, pk, format=None):
        conn_obj = self.get_object(pk)
        data = request.data
        var_ser = serial(conn_obj, data=data)
        var_ser.is_valid(raise_exception=True)
        var_ser.save()

        response = Response()
        response.data = {
            'message': "connection updated successfully",
            'data': var_ser.data
        }
        return response

    #addition starts here........
def add(self,a,b):
    return HttpResponse(
        f"Addition of {a,b} is {a+b}<br><br>\
        substraction of {a, b} is {a - b}<br><br>\
        multiplication of {a, b} is {a * b}<br><br>\
        division of {a, b} is {a / b}"
        )