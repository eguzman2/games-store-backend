from models.user import User
from database.user_db import UserDB

class UserController:
	
	def __init__(self):
		self.USER_DB = UserDB()

	def get_users(self, res_format='list', with_password=False):
		return self.USER_DB.get_users(res_format, with_password)

	def get_user(self, data):
		response = dict()
		response['error'] = True

		id = int(data['id']) if 'id' in data else -1
		with_password = data['with_password'] if 'with_password' else False

		if id == -1:
			response['code'] = '2009'
		else:
			user = self.USER_DB.get_user_by_id(id)
			if user:
				response.update(user.dump(with_password))
				response['code'] = '2010'
				response['error'] = False
			else:
				response['code'] = '2007'

		return response

	def create(self, data):
		response = dict()
		response['error'] = True

		id = self.USER_DB.get_next_id() if not 'id' in data else data['id']
		username = data['username'] if 'username' in data else ''
		first_name = data['first_name'] if 'first_name' in data else ''
		last_name = data['last_name'] if 'last_name' in data else ''
		password = data['password'] if 'password' in data else ''
		user_type = int(data['user_type']) if 'user_type' in data else 2

		if username == '':
			response['code'] = '1002'
		elif self.USER_DB.check_if_username_exists(username):
			response['code'] = '1003'
		else:
			new_user = User(id, username, first_name, last_name,
				password, user_type)
			self.USER_DB.add(new_user)
			response['code'] = '1001'
			response.update(new_user.dump())
			response['error'] = False
		return response

	def edit(self, data):
		response = dict()
		response['error'] = True

		id = int(data['id']) if 'id' in data else -1
		username = data['username'] if 'username' in data else ''
		first_name = data['first_name'] if 'first_name' in data else ''
		last_name = data['last_name'] if 'last_name' in data else ''
		password = data['password'] if 'password' in data else ''

		if id == -1:
			response['code'] = '2006'
		elif username == '':
			response['code'] = '1002'
		elif self.USER_DB.check_if_username_exists(username, id):
			response['code'] = '1003'
		else:
			updated = self.USER_DB.update_user(id, username, 
					first_name, last_name, password)
			if updated:
				response.update(updated.dump())
				response['code'] = '2008'
				response['error'] = False
			else:
				response['code'] = '2007'

		return response

	def login(self, data):
		response = dict()
		response['error'] = True
		
		username = data['username'] if 'username' in data else ''
		password = data['password'] if 'password' in data else ''

		user = self.USER_DB.get_user_by_username(username)
		if user:
			if user.password == password:
				response['code'] = '2001'
				response.update(user.dump())
				response['error'] = False
			else:
				response['code'] = '2003'
		else:
			response['code'] = '2002'
		return response

	def recover_password(self, data):
		response = dict()
		response['error'] = True
		
		username = data['username'] if 'username' in data else ''

		user = self.USER_DB.get_user_by_username(username)
		if user:
			response['password'] = user.password
			response['error'] = False
			response['code'] = '2004'
		else:
			response['code'] = '2005'
		return response