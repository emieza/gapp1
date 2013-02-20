from pyramid.config import Configurator
from resources import Root
import views
import pyramid_jinja2
import os

__here__ = os.path.dirname(os.path.abspath(__file__))


def make_app():
    """ This function returns a Pyramid WSGI application.
    """
    settings = {}
    settings['mako.directories'] = os.path.join(__here__, 'templates')
    
    config = Configurator( root_factory=Root, settings=settings )
    #config.add_renderer('.jinja2', pyramid_jinja2.Jinja2Renderer)
    #config.add_view(views.my_view, context=Root, renderer='mytemplate.jinja2')
    config.add_static_view(name='static',
                           path=os.path.join(__here__, 'static'))
    # les meves views
    config.add_route("home","/")
    config.add_view( views.home_view, route_name="home", renderer="main.mako" )
    config.add_route("page1","/page1")
    config.add_view( views.page1_view, route_name="page1", renderer="page1.mako" )
    config.add_route("crea_event","/crea_event")
    config.add_view( views.crea_event_view, route_name="crea_event", renderer="crea_event.mako" )
    config.add_route("llista_events","/llista_events")
    config.add_view( views.llista_events_view, route_name="llista_events", renderer="llista_events.mako" )
    
    # scan no funciona en GAE!!
    #config.scan()
    return config.make_wsgi_app()

application = make_app()
