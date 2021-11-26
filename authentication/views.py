from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import User
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class DeleteUserView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, user_pk: int, *args, **kwargs) -> Response:
        '''
        This method DELETE removes a user from the database.
        But you can only use this method if you are admin or staff.
        '''
        user = get_object_or_404(User, pk=user_pk)
        user.delete()
        return Response('The user is deleted.', status=HTTP_200_OK)
