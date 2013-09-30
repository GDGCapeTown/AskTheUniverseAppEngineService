# Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions

# Custom importing
from base import BaseHandler
import schema

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class HomepageHandler(BaseHandler):
	def get(self):

		# get the current user
		user_obj = users.get_current_user()

		# Questions to show
		question_objs = []

		# If logged in get the questions we have
		if user_obj:

			# Load questions
			question_objs = schema.UniverseQuestion.get_current_questions(user_obj)

		# Locales
		locales = {

			'show_message': self.request.get('created_question') == '1',
			'show_answered': self.request.get('answered_question') == '1',
			'user_obj': user_obj,
			'question_objs': question_objs,
			'show_question_list': len(question_objs) > 0

		}

		# Render the template
		self.render('main.html', locales)