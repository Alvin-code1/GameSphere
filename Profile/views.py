from .models import PRofileDB
from rest_framework.response import Response
from django.contrib import sessions
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
            'method': 'DEL',
            'body': {},
            'description': 'Eliminar el perfil'
        },
    ]
    return Response(routes)

class ProfileAPIView(APIView):
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        return Response()
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response()
        
    
    def put(self, request,pk):
        profile = get_object_or_404(PRofileDB,pk=pk)
        serializer = ProfileSerializer(profile, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def patch(self, request,pk):
        profile = get_object_or_404(PRofileDB,pk=pk)
        serializer = ProfileSerializer(profile, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
    
    def delete(self, request, pk):
        profile = get_object_or_404(PRofileDB,pk=pk)
        profile.delete()
        return Response()