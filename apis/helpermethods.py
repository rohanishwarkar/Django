from rest_framework.response import Response

def getResponse(status,code,details,data):
    return Response({
        'status':status,
        'code':code,
        'details':details,
        'data':data
    })
