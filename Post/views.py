from rest_framework.response import Response
from .models import PostDB
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class PostAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request, pk):
        profile = request.user.id
        post = get_object_or_404(PostDB,pk=pk,profile=profile)
        return Response(status=status.HTTP_200_OK,data=post.data)
    
    def post(self, request):
        data = request.data.copy()
        data['profile'] = request.user.id
        
        serializer = self.serializer_class(data=data)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk):
        post = get_object_or_404(PostDB,pk=pk)
        serializer = PostSerializer(post, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = get_object_or_404(PostSerializer,pk=pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)