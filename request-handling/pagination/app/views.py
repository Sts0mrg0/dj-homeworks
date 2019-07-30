from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from csv import DictReader
from app.settings import BUS_STATION_CSV
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page = int(request.GET.get('page', 1))
    bus_stations_array = []
    with open(BUS_STATION_CSV, 'r', encoding='cp1251') as csv_file:
        stations_list = DictReader(csv_file)
        stations_rows = list(stations_list)
        for i in range((page-1)*10, (page-1)*10+10):
            bus_stations_array.append({
                'Name': stations_rows[i]['Name'],
                'Street': stations_rows[i]['Street'],
                'District': stations_rows[i]['District']
            })
    if page >= 2:
        params = {'page': page-1}
        prev_page_url = reverse('bus_stations')+ '?' + urlencode(params)
    else:
        prev_page_url = None
    return render_to_response('index.html', context={
        'bus_stations': bus_stations_array,
        'current_page': page,
        'prev_page_url': prev_page_url,
        'next_page_url': reverse('bus_stations')+ '?' + urlencode({'page': page+1}),
    })