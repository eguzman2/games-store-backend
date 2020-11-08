
class User:
	"""
	User types
	1: admin
	2: normal user
	"""
	def __init__(self, id, username, first_name, last_name, 
		password, user_type):
		self.id = id
		self.username = username
		self.first_name = first_name
		self.last_name = last_name
		self.password = password
		self.user_type = user_type

	def dump(self, password=False):
		data = {
			'id': self.id,
			'username': self.username,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'user_type': self.user_type
		}
		if password:
			data['password'] = self.password
		return data