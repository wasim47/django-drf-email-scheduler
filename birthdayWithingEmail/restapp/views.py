from django.shortcuts import render, redirect
import requests
from . models import Customer
from . serializers import CustomerSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from json.decoder import JSONDecodeError

# Create your views here.
def customer_list(request):
    # Get Customer Object List
    list = Customer.objects.all()

    # Convert to serialize data
    seralizer = CustomerSerializer(list, many=True)

    # Convert to Json Data
    jsonData = JSONRenderer().render(seralizer.data)
    return HttpResponse(jsonData, content_type="application/json")


def customer(request, pk):
    try:
        # Get Single Customer Data by Primary key
        singleData = Customer.objects.get(id=pk)

        # Convert to serialize data
        seralizer = CustomerSerializer(singleData)

        # Convert to Json Data
        jsonData = JSONRenderer().render(seralizer.data)
        return HttpResponse(jsonData, content_type="application/json")
    
    except Customer.DoesNotExist:
        res = {"msg": "Data Not Found"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    

@csrf_exempt
def customer_create(request):
    if(request.method == "POST"):
        json_data = request.body

    #Json to Stream convertion
    stream = io.BytesIO(json_data)

    #stream to python type
    python_data = JSONParser().parse(stream)

    #Convert python to complex data
    serilizer = CustomerSerializer(data=python_data)
    if serilizer.is_valid():
        serilizer.save()
        res = {"msg": "Successfully Inserted Data"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serilizer.errors)
    return HttpResponse(json_data, content_type='application/json')   


@csrf_exempt
def customer_update(request):
    try:
        if request.method == 'PUT':
            json_data = request.body

            #Json to Stream convertion
            stream = io.BytesIO(json_data)

            #stream to python type
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            customerData = Customer.objects.get(id=id)

            #Convert python to complex data
            serilizer = CustomerSerializer(customerData, data=python_data, partial=True)
            if serilizer.is_valid():
                serilizer.save()
                res = {"msg": "Successfully Updated Data"}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serilizer.errors)
            return HttpResponse(json_data, content_type='application/json')
    except Customer.DoesNotExist:
        res = {"msg": "Data Not Found"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt
def customer_delete(request):
    try:
        if request.method == 'DELETE':
            json_data = request.body

            #Json to Stream convertion
            stream = io.BytesIO(json_data)

            #stream to python type
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            customerData = Customer.objects.get(id=id)
            customerData.delete()
            res = {"msg": "Successfully Deleted Data"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    except Customer.DoesNotExist:
        res = {"msg": "Data Not Found"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')