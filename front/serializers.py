from rest_framework import serializers
from front.models import Transaction, Client
from front.exceptions import FailedTranasction
from front.tools import clean_number, is_valid_number
from django.contrib.auth.models import User
import logging as log

class WritableClient(serializers.WritableField):
    
    def to_native(self, value):
        return value.cellnum

    def from_native(self, value):
        return value

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'created', 'cellnum')

    def __init__(self, *args, **kwargs):
        log.debug("in ClientSerializer")
        super(serializers.ModelSerializer, self).__init__(*args, **kwargs)

class ClientAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'created', 'cellnum', 'method')

    def __init__(self, *args, **kwargs):
        log.debug("in ClientAddSerializer")
        super(serializers.ModelSerializer, self).__init__(*args, **kwargs)

class TransactionSerializer(serializers.ModelSerializer):
    client = serializers.Field(source='client.cellnum')
    user = serializers.Field(source='user.username')
    class Meta:
        model = Transaction
        fields = ('id', 'created', 'amount', 'currency','client', 'user', 'status')

    def __init__(self, *args, **kwargs):
        log.debug("in TransactionSerializer")
        super(serializers.ModelSerializer, self).__init__(*args, **kwargs)

class TransactionAddSerializer(serializers.ModelSerializer):
    client = WritableClient('client')
    user = serializers.Field(source='user.username')

    class Meta:
        model = Transaction
        fields = ('id', 'created', 'amount', 'client','currency', 'user')

    def __init__(self, *args, **kwargs):
        log.debug("in TransactionAddSerializer")
        super(serializers.ModelSerializer, self).__init__(*args, **kwargs)

    def validate_client(self, attrs, source):
        """
        Check the number well formated.
        """
        log.debug("in validate_client")
        log.debug(attrs[source])
        attrs[source] = clean_number(attrs[source])
        log.debug(attrs[source])
        if not is_valid_number(attrs[source]):
            raise serializers.ValidationError("cellnum is not valid")
        else:
            attrs[source], created = Client.objects.get_or_create(cellnum=attrs[source])
        log.debug(attrs[source])
        return attrs

    def validate_amount(self, attrs, source):
        """
        check the amount is acceptable.
        """
        log.debug("in validate_amount")
        if not 0< attrs[source]<= 50:
            raise serializers.ValidationError("amount is not valid, amount should be between 0 (not included) and 50")
        attrs[source], created = Client.objects.get_or_create(cellnum=attrs[source])
        return attrs

    # def validate(self, attrs):
    #     """
    #     Do the transaction with the carrier
    #     """
    #     log.debug("the value of attrs is : %s" % str(attrs))
    #     # if attrs["cellnum"] == "5147777777":
    #     #     raise FailedTranasction("cellnum is prepaid")
    #     return attrs

class UserSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User

