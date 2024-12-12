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
            posts = PostDB.objects.all().order_by('-id')[:10]
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def modify_reaction_count(request):
    pk = request.data.get('pk')
    action = request.data.get('action')  # 'increase' or 'decrease'
    
    post = get_object_or_404(PostDB, pk=pk, user=request.user)
    
    if action == 'increase':
        post.reaction_count += 1
    elif action == 'decrease':
        post.reaction_count = max(0, post.reaction_count - 1)  # Prevent negative count
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Invalid action'})
    
    post.save()
    return Response(status=status.HTTP_200_OK, data={'reaction_count': post.reaction_count})
