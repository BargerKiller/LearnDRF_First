from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title_no_hello, unique_product_title


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',

    )
    title = serializers.CharField(validators=[
        validate_title_no_hello,
        unique_product_title
    ])

    # email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            'url',
            'owner',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'path'
        ]

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None

        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)
