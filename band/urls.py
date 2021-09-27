from django.urls import path
from . import views

urlpatterns = [
    path('contact-us/', views.view_contact, name='view_contact'),
    path('gigs/', views.view_gigs, name='view_gigs'),
]
