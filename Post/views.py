from rest_framework.response import Response
from .models import PostDB
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class PostAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request, pk=None):
        if request.user.is_authenticated:
            if pk:
                post = get_object_or_404(PostDB, pk=pk, profile=request.user.id)
                serializer = self.serializer_class(post)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else:
                posts = PostDB.objects.filter(profile=request.user.id).order_by('-id')[:10]
                serializer = self.serializer_class(posts, many=True)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        if request.user.is_authenticated:
            data = request.data.copy()
            data['profile'] = request.user.id
            
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, pk):
        if request.user.is_authenticated:
            post = get_object_or_404(PostDB, pk=pk, profile=request.user.id)
            serializer = self.serializer_class(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, pk):
        if request.user.is_authenticated:
            post = get_object_or_404(PostDB, pk=pk, profile=request.user.id)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)