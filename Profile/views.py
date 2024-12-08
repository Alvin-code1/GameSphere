from rest_framework import status
from .models import PRofileDB
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/profile/create',
            'method': 'POST',
            'body': {},
            'description': 'Crear perfil'
        },
        {
            'Endpoint': '/profile/update',
            'method': 'PUT',
            'body': {},
            'description': 'Actualizar el perfil'
        },
        {
            'Endpoint': '/profile/delete',
            'method': 'DELETE',
            'body': {},
            'description': 'Eliminar el perfil'
        },
    ]
    return Response(routes)

class ProfileAPIView(APIView):
    serializer_class = ProfileSerializer

    def get(self, request, pk=None):
        profile = get_object_or_404(PRofileDB, pk=pk)
        serializer = self.serializer_class(profile)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        # Añadir el usuario autenticado a los datos del perfil
        data = request.data.copy()
        data['user'] = request.user.id
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def patch(self, request, pk):
        profile = get_object_or_404(PRofileDB, pk=pk)
        serializer = self.serializer_class(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    def delete(self,request, pk):
        profile = get_object_or_404(PRofileDB, pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
