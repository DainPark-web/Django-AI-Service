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
       from django.core.mail import send_mail
       from django.conf import settings

       # Send email with API key
       subject = 'Your New API Key'
       message = f'Your new API key is: {api_key.raw_key}\n\nPlease store this securely as it cannot be retrieved later.'
       from_email = settings.DEFAULT_FROM_EMAIL
       recipient_list = [request.user.email]
       
       send_mail(
           subject,
           message,
           from_email,
           recipient_list,
           fail_silently=False,
       )
       return Response(serializer.data)
