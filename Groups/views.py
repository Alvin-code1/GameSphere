from django.contrib.auth.models import Group
from rest_framework.response import Response
from .serializers import GroupSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

class GroupAPIView(APIView):
    serializer_class = GroupSerializer

    def get(self,request, _pk):
        group = Group.objects.get(pk=_pk)
        if group.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK,data=group.objects.all)
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.data)
    
    def patch(self, request,pk):
        group = get_object_or_404(Group,pk=pk)
        serializer = GroupSerializer(group, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        group = get_object_or_404(GroupSerializer,pk=pk)
        group.delete()
        return Response(status=status.HTTP_200_OK)
