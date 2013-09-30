# Google Libraries
from google.appengine.ext import ndb

#
# Event Details
# @author Johann du Toit
#
class UniverseQuestion(ndb.Model):
	created_by = ndb.UserProperty(auto_current_user_add=True)
	message = ndb.StringProperty()
	answer = ndb.StringProperty(default=None)
	created = ndb.DateTimeProperty(auto_now_add=True)
	lastupdated = ndb.DateTimeProperty(auto_now_add=True,auto_now=True)

	#
	# Returns the event by it's slug
	#
	@staticmethod
	def get_current_questions(user_obj):

		query_obj = UniverseQuestion.query(UniverseQuestion.created_by != user_obj,UniverseQuestion.answer == None)
		return query_obj.fetch()

	#
	# Returns the event by it's slug
	#
	@staticmethod
	def get_by_user(user_obj):

		query_obj = UniverseQuestion.query(UniverseQuestion.created_by == user_obj)
		return query_obj.fetch()

	#
	# Checks and returns the account_obj for that
	# provider
	#
	@staticmethod
	def get_single_result(query_obj):

		# Get all the accounts with that limit
		item_objs = query_obj.fetch(limit=1)

		# Did we get a account ?
		if item_objs != None and len(item_objs) > 0:

			# Return the first
			return item_objs[0]

		else:

			# Else this is a false request
			return False
