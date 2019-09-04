from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def cola_impresion(request):
    if request.method == 'GET':
        return Response(status = status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response({'received data': request.data.get('imagen').name})

