from rest_framework import serializers
from toys.models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('id','name', 'description','release_date','toy_category','was_included_in_home')





#Manual serializer Cap 3#
# class ToySerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=150)
#     description = serializers.CharField(max_length=250)
#     release_date = serializers.DateTimeField()
#     toy_category = serializers.CharField(max_length=200)
#     was_included_in_home = serializers.BooleanField(required=False)

#     def create(self, validated_data):
#         print("creating...")
#         return Toy.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         print("updating...{}".format(instance.name))
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.release_date = validated_data.get(
#             'release_date', instance.release_date)
#         instance.toy_category = validated_data.get(
#             'toy_category', instance.toy_category)
#         instance.was_included_in_home = validated_data.get(
#             'was_included_in_home', instance.was_included_in_home)
#         instance.save()
#         return instance





#This code are the includes files for shell testing#
# from datetime import datetime
# from django.utils import timezone
# from django.utils.six import BytesIO
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from toys.models import Toy
# from toys.serializers import ToySerializer
