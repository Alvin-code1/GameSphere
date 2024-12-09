from django.core.exceptions import ObjectDoesNotExist
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
        if request.user.is_authenticated():
            try:
                group = Group.objects.get(pk=_pk)
                return Response(status=status.HTTP_200_OK,data=group.objects.all)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        if request.user.is_authenticated():
            try:
                serializer = self.serializer_class(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK,data=serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.data)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def patch(self, request,pk):
        if request.user.is_authenticated():
            try:
                group = get_object_or_404(Group,pk=pk)
                serializer = GroupSerializer(group, data= request.data, partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, pk):
        if request.user.is_authenticated():
            try:
                group = get_object_or_404(GroupSerializer,pk=pk)
                group.delete()
                return Response(status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)