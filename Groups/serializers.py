from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer

class GroupSerializer(ModelSerializer):
    model = Group
    fields = '__all__'