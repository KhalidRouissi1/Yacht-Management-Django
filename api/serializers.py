from rest_framework import serializers
from yachtStore.models import Yacht

class YachtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yacht
        fields = '__all__'