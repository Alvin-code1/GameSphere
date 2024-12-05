from django.contrib.auth.models import Group
from rest_framework.response import Response
from .serializers import GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

class GeoupAPIView(APIView):
    serializer_class = GroupSerializer

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
        group = get_object_or_404(Group,pk=pk)
        serializer = GroupSerializer(group, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def patch(self, request,pk):
        group = get_object_or_404(Group,pk=pk)
        serializer = GroupSerializer(group, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def delete(self, request, pk):
        group = get_object_or_404(GroupSerializer,pk=pk)
        group.delete()
        return Response()
