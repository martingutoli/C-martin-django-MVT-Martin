from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from familia.models import Datos_familia



def info_familia(request):

    familias = Datos_familia.objects.all()

    lista_familia = []

    for familia in familias:
        lista_familia.append(familia.nombre)
        lista_familia.append(familia.fecha_nac)
        lista_familia.append(familia.edad)
        lista_familia.append(familia.relacion)

    datos = {"familiares": lista_familia}

    archivo = open(r"C:\martin\django\MVT+Martin\familiares\familia\template\familiar.html", "r")
    contenido_html = archivo.read()
    archivo.close()

    plantilla = Template(contenido_html)
    contexto = Context (datos)
    doc_renderizar = plantilla.render(contexto)
    return HttpResponse(doc_renderizar)


  
