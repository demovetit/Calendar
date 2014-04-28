#!/usr/bin/env python

import os
import webapp2
import mycalendar.handlers

_WEBAPP_WEB_CONFIG = {
    'webapp2_extras.jinja2': { 
        'template_path': os.path.join(os.path.dirname(__file__), "static", "html"),
        'environment_args' : {
            'auto_reload' : True
        }
    }
}

app = webapp2.WSGIApplication([
    ('/', mycalendar.handlers.Index),
    ('/agenda', mycalendar.handlers.Agenda),
    ('/new', mycalendar.handlers.New)
], debug=True, config=_WEBAPP_WEB_CONFIG)
