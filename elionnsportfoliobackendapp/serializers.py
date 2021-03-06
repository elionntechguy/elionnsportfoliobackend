from .models import Work
from rest_framework import serializers


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'title', 'content', 'link' , 'workimg')