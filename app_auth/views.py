from django.contrib.auth.models import User
from .serializers import SignupSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer
