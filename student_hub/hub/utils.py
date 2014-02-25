from django.http import HttpResponseRedirect, HttpResponse
import os
from django.contrib.gis.geoip import GeoIP

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def return_city_country(ip, current_user):
    g = GeoIP()
    location=g.city(ip)
    try:
        current_user.city=location['city']
        current_user.country=location['country_code']
        current_user.latitude=location['latitude']
        current_user.longitude=location['longitude']
        current_user.save()
    except TypeError:
        city='local machine'
        country='local'

#def find_tutor(query):
	