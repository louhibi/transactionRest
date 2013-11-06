#front app
from front.models import Transaction, Client
from front.serializers import TransactionSerializer
from front.serializers import UserSerializer
from front.serializers import ClientSerializer
from front.serializers import ClientAddSerializer
from front.serializers import TransactionAddSerializer
#rest app
from rest_framework import generics
from rest_framework import permissions
#django
from django.contrib.auth.models import User

class TransactionList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = "client"

    def pre_save(self, obj):
        obj.user = self.request.user

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TransactionAddSerializer
        else:
            return TransactionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        try:
            return Transaction.objects.filter(user=user)
        except TypeError:
            #if no user
            return Transaction.objects.filter(user=0)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def pre_save(self, obj):
        obj.user = self.request.user

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ClientAddSerializer
        else:
            return ClientSerializer


class ClientDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
