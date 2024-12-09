from rest_framework import status
from .models import PRofileDB
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ProfileAPIView(APIView):
    serializer_class = ProfileSerializer

    def get(self, request):
        pk = request.user.id
        profile = get_object_or_404(PRofileDB, pk=pk)
        serializer = self.serializer_class(profile)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        # Añadir el usuario autenticado a los datos del perfil
        data = request.data.copy()
        data['user'] = request.user.id
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def patch(self, request):
        pk = request.user.id
        profile = get_object_or_404(PRofileDB, pk=pk)
        serializer = self.serializer_class(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    def delete(self,request):
        pk = request.user.id
        profile = get_object_or_404(PRofileDB, pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
