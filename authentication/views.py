from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from app.models import Project
from .models import User
from .serializers import RegisterSerializer
from authentication.serializers import UserSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(user_projects__id=self.kwargs['project_pk'])
