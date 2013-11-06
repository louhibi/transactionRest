from rest_framework.exceptions import APIException

class FailedTranasction(APIException):
    d = {"descrption": "Carrier not supported",
         "status":"FAILED"
        }
    detail = d
    status_code = 501