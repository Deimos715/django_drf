from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def hello_world(request):
    return JsonResponse({'message': 'Hello World!'})


@api_view()
def hello_world_drf(request):
    return Response({'message': 'Hello World!'})
