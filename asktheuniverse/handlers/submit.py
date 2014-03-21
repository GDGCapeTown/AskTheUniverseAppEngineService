# Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions
from google.appengine.api import mail

# Custom importing
from base import BaseHandler
import asktheuniverse.schema as schema

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class SubmitHandler(BaseHandler):
	def post(self):

		# Get the posted message
		text_str = self.request.POST.get('message')

		# Setup our model
		question_obj = schema.UniverseQuestion()
		question_obj.message = text_str
		question_obj.put()

		# redirect and tell the homepage we checked
		self.redirect('/?created_question=1')

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class UpdateQuestionHandler(BaseHandler):
	def post(self):

		# Get the posted message
		question_id = self.request.POST.get('question_id')
		message_str = self.request.POST.get('message')

		# Setup our model
		question_obj = schema.UniverseQuestion.get_by_id(long(question_id))
		if question_obj != None:

			mail.send_mail('noreply@example.com', question_obj.created_by.email(), 'Your question was answered', 'The answer to "' + question_obj.message + '" is "' + message_str + '"')

			# Save it
			question_obj.answer_by = users.get_current_user()
			question_obj.answer = message_str
			question_obj.put()

		# redirect and tell the homepage we checked
		self.redirect('/?answered_question=1')
