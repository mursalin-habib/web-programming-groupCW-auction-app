from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from users.api.serializers import UserSerializer
from django.contrib.auth import get_user_model

from users.models import CustomUser
from rest_framework import generics, status


class CurrentUserView(APIView):
    def get(self, request):
        print(self.request.user.id)
        user = CustomUser.objects.get(id=self.request.user.id)
        print(user.image)
        return Response(dict({
            'id': user.id,
            'dob': user.dob,
            'email': user.email,
            'city': user.city,
            'image': str(user.image if user.image else '')
        }))


class UserUpdateView(generics.UpdateAPIView):
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     print(serializer)
    #     serializer.is_valid(raise_exception=True)
    #     print(serializer)
    #     self.perform_update(serializer)
    #     return Response(dict({
    #         'id': instance.id,
    #         'username': instance.username,
    #         'dob': instance.dob,
    #         'email': instance.email,
    #         'city': instance.city,
    #         # 'profile_img': user.profile_picture,
    #     }), status=status.HTTP_201_CREATED)
