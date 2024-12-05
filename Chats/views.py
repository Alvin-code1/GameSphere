from .models import ChatsDB, MessageDB
from rest_framework.response import Response
from .serializers import ChatsSerializer, MessageSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

class ChatAPIView(APIView):
    serializer_class = ChatsSerializer

    def get(self, request):
        return Response()
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response()
        
    
    def put(self, request,pk):
        chat = get_object_or_404(ChatsDB,pk=pk)
        serializer = ChatsSerializer(chat, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def patch(self, request,pk):
        chat = get_object_or_404(ChatsDB,pk=pk)
        serializer = ChatsSerializer(chat, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def delete(self, request, pk):
        chat = get_object_or_404(ChatsDB,pk=pk)
        chat.delete()
        return Response()

class MessageAPIView(APIView):
    serializer_class = MessageSerializer

    def get(self, request):
        return Response()
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response()
        
    
    def put(self, request,pk):
        message = get_object_or_404(MessageDB,pk=pk)
        serializer = MessageSerializer(message, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def patch(self, request,pk):
        message = get_object_or_404(MessageDB,pk=pk)
        serializer = MessageSerializer(message, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def delete(self, request, pk):
        message = get_object_or_404(MessageDB,pk=pk)
        message.delete()
        return Response()
