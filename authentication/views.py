from app.models import Project
from app.permissions import IsAuthorOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from authentication.serializers import UserSerializer

from .models import User
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def list(self, request, project_pk):
        queryset = User.objects.filter(user_projects__id=project_pk)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, project_pk, user_id, *args, **kwargs):
        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise ValidationError("The user doesn't exist.")
        project = Project.objects.get(pk=project_pk)
        if user in project.users.all():
            raise ValidationError("The user is already in the list.")
        else:
            project.users.add(user.id)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, project_pk, user_id, *args, **kwargs):
        project = Project.objects.get(pk=project_pk)
        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise ValidationError("The user doesn't exist.")
        project.users.remove(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
