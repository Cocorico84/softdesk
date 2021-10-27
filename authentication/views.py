from app.permissions import IsAuthorOrReadOnly
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet

from authentication.serializers import UserSerializer

from .models import User
from .serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    # TODO surcharger create() pour ajouter un user existant et ne pas en créer un en utilisant un ViewSet

    def get_queryset(self):
        return User.objects.filter(user_projects__id=self.kwargs['project_pk'])
