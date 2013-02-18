# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPFound
from google.appengine.api import users

from pyramid.view import (
    view_config,
    forbidden_view_config,
)

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
    

