from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from Proyecto_API.api.models import Videogames
# Create your views here.
class VideoViews(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        if (id > 0):
            juegos = list(Videogames.objects.filter(id=id).values())
            if len(juegos) > 0:
                juego = juegos[0]
                datos = {'message': "Success", 'juego': juego}
            else:
                datos = {'message': "juego not found..."}
            return JsonResponse(datos)
        else:
            juegos = list(Videogames.objects.values())
            if len(juegos) > 0:
                datos = {'message': "Success", 'juegos': juegos}
            else:
                datos = {'message': "Juegos not found..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        # print(jd)
        Videogames.objects.create(name=jd['name'], published_year=jd['published_year'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        juegos = list(Videogames.objects.filter(id=id).values())
        if len(juegos) > 0:
            juegos = Videogames.objects.get(id=id)
            juegos.name = jd['name']
            juegos.published_year = jd['published_year']
            juegos.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Game not found..."}
        return JsonResponse(datos)


    def delete(self, request,id):
        juegos = list(Videogames.objects.filter(id=id).values())
        if len(juegos) > 0:
            Videogames.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Game not found..."}
        return JsonResponse(datos)