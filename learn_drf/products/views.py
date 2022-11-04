from rest_framework import generics, mixins

from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionsMixin, UserQuerySetMixin


class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionsMixin,
    generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_staff_view = False

    def perform_create(self, serializer):
        content = serializer.validated_data.get('content')
        if content is None:
            content = serializer.validated_data.get('title')
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self):
    #     request = self.request
    #     qs = super().get_queryset()
    #     if not request.user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)


class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionsMixin,
    generics.RetrieveAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionsMixin,
    generics.UpdateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionsMixin,
    generics.DestroyAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ProductMixinView(
    UserQuerySetMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # class ProductDeleteAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductListAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
