from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from .serializers import GroupSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class GroupAPIView(APIView):
    serializer_class = GroupSerializer

    def get(self, request, pk=None):
        if request.user.is_authenticated:
            if pk is not None:
                group = get_object_or_404(Group, pk=pk)
                serializer = self.serializer_class(group)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else:
                groups = Group.objects.all()
                serializer = self.serializer_class(groups, many=True)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, pk):
        if request.user.is_authenticated:
            group = get_object_or_404(Group, pk=pk)
            serializer = self.serializer_class(group, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        if request.user.is_authenticated:
            group = get_object_or_404(Group, pk=pk)
            group.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)