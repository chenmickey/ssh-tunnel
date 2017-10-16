from app.schema.auth import Auth


class AuthModel(object):
	def __init__(self):
		self.auth_entity = Auth()
	
	def get_user_by_id(self, _id):
		self.auth_entity.search()
