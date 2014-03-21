# Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions

# Custom importing
from base import BaseHandler
import asktheuniverse.schema as schema

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class ListAllQHandler(BaseHandler):
	def get(self):

		if users.is_current_user_admin():

			# Get all the questions
			question_objs = schema.UniverseQuestion.query().fetch()

			self.render('listing.html', {

				'user_obj': users.get_current_user(),
				'question_objs': question_objs

			})

		else:

			self.redirect('/')