from django.shortcuts import render
from django.conf import settings
import requests
import datetime


def view_contact(request):
    """ A view to return the Contact Us page """
    template = 'band/contact.html'
    return render(request, template)


def view_gigs(request):
    """ A view to return the Upcoming Gigs page """
    requestURL = settings.SONGKICK_API
    result = requests.get(requestURL).json()
    events = result['resultsPage']['results']['event']
    events_dict = []
    for event in events:
        bands = event['performance']
        band_line_up = []
        for i in range(len(bands)):
            band_line_up.append(bands[i]['displayName'])
        current_event = {
            'venue_name': event['venue']['displayName'],
            'band_line_up': band_line_up,
            'date': event['start']['date'],
            'time': event['start']['time'][:-3],
            'location': event['location']['city'],
            'songkick_link': event['uri']
        }
        events_dict.append(current_event)
    print(events_dict[0]['venue_name'])
    template = 'band/gigs.html'
    return render(request, template, {'content': events_dict})
