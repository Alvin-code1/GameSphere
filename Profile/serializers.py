from rest_framework.serializers import ModelSerializer
from .models import PRofileDB

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = PRofileDB
        fields = ['username','url','profile_pic','back_profile_pic','description']