# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPFound
from google.appengine.api import users
import datetime, logging

from models import *

def my_view(request):
    return {'project':'gapp1'}

# al GAE no li agraden els decorators @view_config
def home_view( request ):
    user = users.get_current_user()
    nomusuari = None
    if user:
        nomusuari = user.nickname()
    return {"project":"gapp1", "usuari": nomusuari }
    
def page1_view( request ):
    return {"project":"gapp1"}
    
def llista_events_view( request ):
    events = []
    query = Event.gql('ORDER BY time')
    for event in query.fetch(10):
        events.append( event )
    return {"project":"gapp1","events":events}

    
def crea_event_view( request ):
    logging.debug("entrant")
    if request.POST.get("titol"):
        # Create an event in the datastore.
        user = users.get_current_user()
        userid = "ningu"
        if user:
            userid = user.user_id()
        new_event = Event(title = request.POST.get('titol'),
                          creator = userid,
                          # Take the time string passing in by JavaScript in the
                          # form and convert to a datetime object.
                          time = datetime.datetime.strptime(
                                 request.POST.get('datetimestamp'), '%d/%m/%Y %H:%M'),
                          description = request.POST.get('descripcio'),
                          location = request.POST.get('lloc'))
        new_event.put()
        logging.debug("processant event")

        # Associate each of the attendees with the event in the datastore.
        #attendee_list = []
        #if self.request.get('attendees'):
        #    attendee_list = self.request.get('attendees').split(',')
        #    if attendee_list:
        #        for attendee in attendee_list:
        #            new_attendee = Attendee(email=attendee.strip(), event=new_event)
        #            new_attendee.put()    
    
    return {"project":"gapp1"}

