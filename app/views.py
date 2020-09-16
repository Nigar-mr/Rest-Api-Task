import logging

from django.shortcuts import render, get_object_or_404
from jsonify.convert import jsonify

from rest_framework import generics, permissions, request, status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .serializers import ProductsSerializers, CategorySerializers, SaleSerializer
from .models import ProductsCategory, Products


# Create your views here.

class Stock(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CategorySerializers

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logging.info('Category is created')
            return Response({
                "category": serializer.data
            },
                status=status.HTTP_201_CREATED)
        else:
            return Response({
                "category": "ALready exsist"
            })

    def get(self, request):
        category = ProductsCategory.objects.all()
        serializer = CategorySerializers(category,  many=True)
        return Response(serializer.data)

class Product(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductsSerializers

    def post(self, request, *args, **kwargs):
        serializer = ProductsSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "data": serializer.data
        })

    def get(self, request):
        all_products = Products.objects.all()
        serializer = ProductsSerializers(all_products, many=True)
        return Response(serializer.data)


class Sale(APIView):
    permission_classes = (permissions.AllowAny,)

    def put(self, request, name):
        products = Products.objects.filter(name=name).first()
        all_count = Products.objects.values_list('count', flat=True)[0]
        count = request.data['count']
        if all_count - count >= 0:
            res = all_count - count
            result = {"count": res}
            serializer = SaleSerializer(instance=products, data=result)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "xxx"})
        else:
            return Response({"message": "Not enough produce"})
