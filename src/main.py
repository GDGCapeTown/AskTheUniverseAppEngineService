#!/usr/bin/env python

# Python Libs
import webapp2
from webapp2_extras import routes
import jinja2
import os
import urllib

# Setup the Handlers
from handlers.home import HomepageHandler
from handlers.auth import LoginHandler, LogoutHandler
from handlers.submit import SubmitHandler, UpdateQuestionHandler

# General Config for our web application
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'secret_key_for_session_here',
}

# Startup our app with the routes we are
# going to configure now
app = webapp2.WSGIApplication([

	('/', HomepageHandler),
	('/login', LoginHandler),
	('/logout', LogoutHandler),
	('/submit', SubmitHandler),
	('/answer', UpdateQuestionHandler)

], debug=True, config=config)