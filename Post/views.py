from rest_framework.response import Response
from .models import PostDB
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def handle_post_request(request):
    action = request.data.get('action')
    
    if action == 'retrieve':
        pk = request.data.get('pk')
        if pk:
            post = get_object_or_404(PostDB, pk=pk, user=request.user)
            serializer = PostSerializer(post)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            posts = PostDB.objects.filter(user=request.user).order_by('-id')[:10]
            serializer = PostSerializer(posts, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    elif action == 'create':
        data = request.data.copy()
        data['user'] = request.user
        data['reaction_count'] = 0  # Initialize reaction count
        data['comments'] = []  # Initialize comments as an empty list
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    elif action == 'update':
        pk = request.data.get('pk')
        post = get_object_or_404(PostDB, pk=pk, user=request.user)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    elif action == 'delete':
        pk = request.data.get('pk')
        post = get_object_or_404(PostDB, pk=pk, user=request.user)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Invalid action'})
