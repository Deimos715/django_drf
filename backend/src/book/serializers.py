from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, default='Django REST Framework')
    author = serializers.CharField(max_length=100)