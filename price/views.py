from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.reverse import reverse_lazy
from price.models import CustomUser, Category, Product
from price.serializers import ProductSerializer, CustomUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


### CategorySerializer,

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


###########################CategoryViewSet (без пользователей, както совсем
# пустынно, сделаем вывод списка CustomUserList, создание на ендпоинте  rest-auth/registration/, удаление
# на ендпоинте CustomUser_detail/<pk>)

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    success_url = reverse_lazy('price:product')
    # permission_classes = (AllowAny)#,IsAuthenticated,)  ###


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Custom permission to only allow owners of an object to edit it.
        """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwnerOrReadOnly,)

####################### Ниже пока закомментирую, но вроде это лишнее.  permission_classes = (IsOwnerOrReadOnly,) работает
# def create(self, request, *args, **kwargs):
#     if self.request.user.seller:
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#     return Response({'Message': 'You have no permission to create'},
#                     status=status.HTTP_405_METHOD_NOT_ALLOWED)  # PermissionError('No chance to make a product')
#
# def perform_create(self, serializer):
#     serializer.save()

# def update(self, request, *args, **kwargs):
#     instance = self.get_object()
#     if self.request.user.seller:
#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#     return Response({'Message': 'You have no permission to create'},
#                     status=status.HTTP_405_METHOD_NOT_ALLOWED)
# def perform_update(self, serializer):
#     serializer.save()
#
# def update(self, request, *args, **kwargs):
#     instance = self.get_object()
#     instance.name = request.data.get("name")
#     instance.save()
#
#     serializer = self.get_serializer(instance)
#     serializer.is_valid(raise_exception=True)
#     self.perform_update(serializer)
#
#     return Response(serializer.data)
