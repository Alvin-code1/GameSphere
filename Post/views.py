from rest_framework.response import Response
from .models import PostDB
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

class PostAPIView(APIView):
    serializer_class = PostSerializer

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
        post = get_object_or_404(PostDB,pk=pk)
        serializer = PostSerializer(post, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def patch(self, request,pk):
        post = get_object_or_404(PostDB,pk=pk)
        serializer = PostSerializer(post, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def delete(self, request, pk):
        post = get_object_or_404(PostSerializer,pk=pk)
        post.delete()
        return Response()
