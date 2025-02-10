from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ai_keys.models import AiKey
from ai_keys.serializers import AiKeyCreateSerializer
# Create your views here.
class AiKeyView(APIView):
    permission_classes = [IsAuthenticated]

class AiKeyCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
       api_key = AiKey.objects.create(user=request.user)
       serializer = AiKeyCreateSerializer(api_key)
       return Response(serializer.data)
