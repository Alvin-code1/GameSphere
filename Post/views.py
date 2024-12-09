from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from .models import PostDB
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class PostAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request, pk):
        if request.user.is_authenticated():
            try:
                profile = request.user.id
                post = get_object_or_404(PostDB,pk=pk,profile=profile)
                return Response(status=status.HTTP_200_OK,data=post.data)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        if request.user.is_authenticated():
            data = request.data.copy()
            data['profile'] = request.user.id
            
            serializer = self.serializer_class(data=data)
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request,pk):
        if request.user.is_authenticated():
            try:
                post = get_object_or_404(PostDB,pk=pk)
                serializer = PostSerializer(post, data= request.data, partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK,data=serializer.data)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, pk):
        if request.user.is_authenticated():
            try:
                post = get_object_or_404(PostSerializer,pk=pk)
                post.delete()
                return Response(status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)