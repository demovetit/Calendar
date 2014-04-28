#!/usr/bin/env python

import webapp2
import mycalendar.handlers

app = webapp2.WSGIApplication([
    ('/', mycalendar.handlers.Event),
], debug=True)
