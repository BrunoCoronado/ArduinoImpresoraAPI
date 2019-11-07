from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from django.http import JsonResponse
from .models import Imagen
from base64 import b64decode
import json
from django.http import HttpResponse
import requests

# Create your views here.
@api_view(['GET','POST'])
def ingresar_cola(request):
    if request.method=='POST':
        cont1=Imagen.objects.order_by("cadena").count()
        
        cont=0
        if cont1!=0:
            obj_list=Imagen.objects.all()[0] 
            cont=obj_list.cadena1+1
        
        #cont=Imagen.objects.order_by("cadena").count()+1


        img=request.data.get('image')

        splitGcode=img.split("\n")
        
        i=1
        tam=len(splitGcode)
        print(img)
        almacenar=""
        contadorPaquete = 0
        while i<=tam:
            if contadorPaquete<50:
                almacenar+=splitGcode[i-1]+"\n"
            if (i%20) == 0:
                if(i + 1 == tam):
                    almacenar+="$"
                aux=Imagen()
                aux.newImagen(almacenar,cont)
                #print(almacenar)
                aux.save()
 
                contadorPaquete = 0
        #        print("\npaquete no. " + str(i-1) + "\n" + almacenar)
                almacenar=""
            i+=1
            contadorPaquete+=1   
        if(almacenar != ""):
            aux=Imagen()
            almacenar+="$"
            aux.newImagen(almacenar,cont)
            #print(almacenar)
            almacenar=""
            aux.save()

         #   print("\npaquete no. " + str(i + 1) + "\n" + almacenar)
            

    return Response({'received data'})

@api_view(['GET','POST'])
def imprimir_cola(request,entero):
    if request.method=='GET':
        cont=Imagen.objects.order_by("cadena").count()
        
        response_data={}

        booleano=0

        if cont==0:
            response_data['gcode']=""
        else:
            print(cont)
            #obj_list=Imagen.objects.all()[cont-1] 
            obj_list=Imagen.objects.all().first()
            response_data['gcode'] = obj_list.cadena 
            booleano=obj_list.cadena1
            if entero==booleano:
                obj_list.delete()    

        if entero!=booleano:
            response_data={}
            response_data['gcode']=""
        

        return HttpResponse(json.dumps(response_data), content_type="application/json")


#url/id
#url/6
#request.params.id 


@api_view(['GET','POST'])
def obtener_id(request):
    if request.method=='GET':    
        
        
        response_data={}
        cont=Imagen.objects.order_by("cadena").count()
        if cont!=0:        
            obj_list=Imagen.objects.all().first()
            response_data['id']=obj_list.cadena1
        else:
            response_data={}
            response_data['id']="-1"
        return HttpResponse(json.dumps(response_data), content_type="application/json")




@api_view(['GET','POST'])
def prueba(request,entero):
    if request.method=='GET':
        texto="pp"
        response_data = {}
        response_data['gcode'] = entero
        
        return HttpResponse(json.dumps(response_data), content_type="application/json")
       

