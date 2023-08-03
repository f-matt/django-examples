from rest_framework import serializers
from main.models import Model1, Model2

class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model1
        fields = ('id1', 'id2', 'col1')


class Model2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model2
        fields = ('id', 'model1_id1', 'model1_id2', 'col1')