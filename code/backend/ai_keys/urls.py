from django.urls import path
from ai_keys.views import AiKeyCreateView

urlpatterns = [
    path('create/', AiKeyCreateView.as_view()),
]   