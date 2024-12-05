from .models import PostDB
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    model = PostDB
    fields = '__all__'