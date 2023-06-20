import math
from django.shortcuts import render
from django.views import View
from yandex_map.forms import Coordinates


class YandexMap(View):
    MAP_URL = 'https://yandex.ru/maps/?ll={}%2C{}&z={}'
    E_CONST = 0.0818191908426
    template = 'maps/index.html'

    def _get_coordinate(self, lon, lat, zoom):
        rho = (2 ** (zoom + 8)) / 2
        beta = (math.pi * lat) / 180
        phi = (1 - (self.E_CONST * math.sin(beta))) / (
                1 + (self.E_CONST * math.sin(beta)))
        theta = math.tan((math.pi / 4) + (beta / 2)) * (phi ** (self.E_CONST / 2))

        x_p = rho * (1 + lon / 180)
        y_p = rho * (1 - math.log(theta) / math.pi)
        return math.floor(x_p / 256), math.floor(y_p / 256)

    def get(self, request):
        context = {}
        if request.GET:
            lon = float(request.GET.get('coordinate_x'))
            lat = float(request.GET.get('coordinate_y'))
            zoom = float(request.GET.get('zoom'))

            x_p, y_p = self._get_coordinate(lon, lat, zoom)
            url = self.MAP_URL.format(lon, lat, zoom)
            context = {
                'coordinate': {'x': x_p, 'y': y_p, 'url': url},
            }

        form = Coordinates()
        context = {
            'forms': form,
            **context
        }
        return render(request, self.template, context)
