from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from products.serializers import ProductSerializer


class FirstApiView(APIView):

    def get(self, request, *args, **kwargs):
        instance = Product.objects.all().order_by('?').first()
        data = {}
        if instance:
            data = ProductSerializer(instance).data
        print(data)
        return Response(data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            data = serializer.data
            return Response(data)
