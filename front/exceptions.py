from rest_framework.exceptions import APIException

class FailedTranasction(APIException):
    detail = "Failed transaction"
    status_code = 601