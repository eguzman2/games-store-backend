import json

class UserDB:

	def __init__(self):
		self.users = []

	def add(self, user):
		self.users.append(user)

	def get_users(self, res_format, with_password):
		if res_format == 'json':
			return json.dumps([user.dump(with_password) for user in self.users])
		else:
			return self.users

	def get_user_by_username(self, username):
		user = False
		for u in self.users:
			if u.username == username:
				user = u
				break
		return user

	def get_user_by_id(self, id):
		user = False
		for u in self.users:
			if u.id == id:
				user = u
				break
		return user

	def check_if_username_exists(self, username='', id=-1):
		"""
		param id: si encuentra una coincidencia, la omite al 
			tratarse del mismo registro
		"""
		if not username:
			return True
		for user in self.users:
			if user.username == username and user.id != id:
				return True
		return False

	def get_next_id(self):
		self.sort()
		if len(self.users) == 0:
			return 1
		return self.users[-1].id + 1

	def update_user(self, id, username, 
					first_name, last_name, password):
		for user in self.users:
			if user.id == id:
				user.username = username
				user.first_name = first_name
				user.last_name = last_name
				user.password = password
				return user
		return False

	def sort(self):
		n = len(self.users)
		for i in range(n-1):
			flag = 0
			for j in range(n-1):
				if self.users[j].id > self.users[j+1].id:
					tmp = self.users[j]
					self.users[j] = self.users[j+1]
					self.users[j+1] = tmp
					flag = 1
			if flag == 0:
				break
