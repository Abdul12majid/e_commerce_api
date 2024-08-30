from rest_framework import serializers
from hackathon.models import Product


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=Product
		fields=('id', 'name', 'price', 'category', 'description',)


class Product_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Product
		fields=('id', 'name', 'price',)