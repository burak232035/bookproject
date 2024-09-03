from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


from rest_framework.response import Response
from rest_framework.views import APIView

class ApiTestView(APIView):
    def get(self, request, mtyp_id=None):
        try:
            return Response("get api")
        except Exception as ex:
            print("Controller(api_test/GET) ERROR : ", ex)
            return Response(ex)

    def post(self, request, mtyp_id=None):
        try:
            return Response("post api")
        except Exception as ex:
            print("Controller(api_test/POST) ERROR : ", ex)
            return Response(ex)

    def put(self, request, mtyp_id=None):
        try:
            return Response("put api")
        except Exception as ex:
            print("Controller(api_test/PUT) ERROR: ", ex)
            return Response(ex)

    def delete(self, request, mtyp_id=None):
        try:
            return Response("delete api")
        except Exception as ex:
            print("Controller(model_type/DELETE) ERROR : ", ex)
            return Response(ex)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer