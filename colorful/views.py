from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .serializer import AddressSerilaizer
from . models import Address
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        address=Address.objects.all()
        serilaizer=AddressSerilaizer(address, many=True)
        return JsonResponse(serilaizer.data, safe=False)
    if request.method=='POST':
        serilaizer=AddressSerilaizer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
        return JsonResponse(serilaizer.data, safe=False)
    return HttpResponse(),
@api_view(['GET','DELETE'])
def details(request,id):
    try:
        address=Address.objects.get(pk=id)
    except Address.DoesNotExist:
        return JsonResponse({'error':'Data not Available'})
    if request.method=='GET':
        serilaizer=AddressSerilaizer(address)
        return JsonResponse(serilaizer.data)
    elif request.method=='DELETE':
        address.delete()
        return JsonResponse({},status=204)
    return HttpResponse()