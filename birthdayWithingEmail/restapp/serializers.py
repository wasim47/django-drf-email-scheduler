from rest_framework import serializers
from . models import Customer

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    contact = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=250)
    date_of_birth = serializers.DateField()

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
    
    # Updatea data into database using serializer
    def update(self, instace, validated_data):
        instace.name = validated_data.get('name', instace.name)
        instace.contact = validated_data.get('contact', instace.contact)
        instace.email = validated_data.get('email', instace.email)
        instace.address = validated_data.get('address', instace.address)
        instace.date_of_birth = validated_data.get('date_of_birth', instace.date_of_birth)
        instace.save()
        return instace