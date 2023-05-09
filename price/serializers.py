from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from price.models import CustomUser, Product, Category, tax, bank_comission, author_our_comission


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['seller', ]


class CustomRegisterSerializer(RegisterSerializer):
    seller = CustomUserSerializer(required=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # print('============ validated_data.pop(price_value)', validated_data.pop('price_value'))
        user = validated_data.get("user", None)
        a = validated_data.pop('price_value')
        b = a / 100 * tax
        c = a / 100 * bank_comission
        d = a / 100 * author_our_comission
        price_value = a + b + c + d
        product_name = validated_data.get("product_name", None)
        product_description = validated_data.get("product_description", None)
        category = validated_data.get("category", None)

        return Product.objects.create(user=user, product_name=product_name, product_description=product_description,
                                      category=category, price_value=price_value)

    def update(self, instance, validated_data):
        if instance.user != validated_data['user']:
            instance.user = validated_data['user']

        if instance.price_value != validated_data['price_value']:
            a = validated_data['price_value']
            b = a / 100 * tax
            c = a / 100 * bank_comission
            d = a / 100 * author_our_comission
            instance.price_value = a + b + c + d

        if instance.product_name != validated_data['product_name']:
            instance.product_name = validated_data['product_name']

        if instance.product_description != validated_data['product_description']:
            instance.product_description = validated_data['product_description']

        if instance.category != validated_data['category']:
            instance.category = validated_data['category']
        instance.save()
        return instance
