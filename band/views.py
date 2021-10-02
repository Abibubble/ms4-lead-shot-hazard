from django.shortcuts import render
from django.conf import settings
import requests
import calendar


def view_contact(request):
    """
    A view to return the Contact Us page
    """

    template = 'band/contact.html'
    return render(request, template)


def view_gigs(request):
    """
    A view to return the Upcoming Gigs page
    """

    requestURL = settings.SONGKICK_API
    result = requests.get(requestURL).json()
    events = result['resultsPage']['results']['event']
    events_dict = []
    for event in events:
        bands = event['performance']
        band_line_up = []
        for i in range(len(bands)):
            band_line_up.append(bands[i]['displayName'])

        week_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
        date = event['start']['date']
        year = int(date[:-6])
        month = int(date[5:7])
        day = int(date[8:])

        current_event = {
            'venue_name': event['venue']['displayName'],
            'band_line_up': band_line_up,
            'year': year,
            'month': calendar.month_name[month],
            'day': day,
            'weekday': week_days[calendar.weekday(year, month, day)],
            'time': event['start']['time'][:-3],
            'location': event['location']['city'],
            'songkick_link': event['uri']
        }
        events_dict.append(current_event)

    template = 'band/gigs.html'
    return render(request, template, {'content': events_dict})
