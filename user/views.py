from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from rest_framework.generics import RetrieveUpdateAPIView
# from .renderers import UserJSONRenderer

from .serializers import RegistrationSerializer, LoginSerializer


# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     permission_classes = (IsAuthenticated,)

#     serializer_class = UserSerializer

#     def retrieve(self, request, *args, **kwargs):
#         # There is nothing to validate or save here. Instead, we just want the
#         # serializer to handle turning our `User` object into something that
#         # can be JSONified and sent to the client.
#         serializer = self.serializer_class(request.user)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         user_data = request.data.get('user', {})

#         serializer_data = {
#             'username': user_data.get('username', request.user.username),
#             'email': user_data.get('email', request.user.email),

#             'profile': {
#                 'bio': user_data.get('bio', request.user.profile.bio),
#                 'image': user_data.get('image', request.user.profile.image)
#             }
#         }

#         # Here is that serialize, validate, save pattern we talked about
#         # before.
# serializer = self.serializer_class(
#     request.user, data=serializer_data, partial=True
# )
# serializer.is_valid(raise_exception=True)
# serializer.save()

# return Response(serializer.data, status=status.HTTP_200_OK)


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        print(request.data)

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()

        # return Response(serializer.data)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        print(request.data)

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)

        # return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid()

        serializer.validated_data

        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserSerializer(serializers.HyperlinkedModelSerializer):

#     class UserSerializer(serializers.HyperlinkedModelSerializer):
#         pets = serializers.HyperlinkedRelatedField(
#             view_name='pet_detail',
#             many=True,
#             read_only=True
#         )
#         password = serializers.CharField(write_only=True)
#         email = serializers.CharField(write_only=True)

#         def create(self, validated_data):
#             user = User.objects.create(
#                 username=validated_data['username'],
#                 email=validated_data['email'],
#                 first_name=validated_data['first_name'],
#             )
#             user.set_password(validated_data['password'])
#             user.save()
#             return user

#         class Meta:
#             model = User
#             fields = ('id', 'username', 'pets',
#                       'first_name', 'email', 'password')


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
