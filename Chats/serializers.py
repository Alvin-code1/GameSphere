from .models import ChatsDB, MessageDB
from rest_framework.serializers import ModelSerializer

class ChatsSerializer(ModelSerializer):
    model = ChatsDB
    fields = '__all__'

class MessageSerializer(ModelSerializer):
    model = MessageDB
    fields = '__all__'