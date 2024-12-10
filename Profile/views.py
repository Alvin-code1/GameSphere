from rest_framework import status
from .models import PRofileDB
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ProfileAPIView(APIView):
    serializer_class = ProfileSerializer

    def get_profile(self, user_id):
        return get_object_or_404(PRofileDB, pk=user_id)

    def get(self, request, pk=None):
        if request.user.is_authenticated:
            if pk is None:
                pk = request.user.id  # Use the authenticated user's ID if no pk is provided
            profile = self.get_profile(pk)
            serializer = self.serializer_class(profile)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        if request.user.is_authenticated:
            data = request.data.copy()
            data['user'] = request.user.id
        
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        if request.user.is_authenticated:
            profile = self.get_profile(request.user.id)
            serializer = self.serializer_class(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        if request.user.is_authenticated:
            profile = self.get_profile(request.user.id)
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)