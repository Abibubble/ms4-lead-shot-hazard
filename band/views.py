from django.shortcuts import render


def view_contact(request):
    """ A view to return the Contact Us page """
    return render(request, 'band/contact.html')


def view_gigs(request):
    """ A view to return the Upcoming Gigs page """
    return render(request, 'band/gigs.html')
