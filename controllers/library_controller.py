from database.library_db import LibraryDB


class LibraryController:
	
	def __init__(self):
		self.LIBRARY_DB = LibraryDB()

	def get_game_ids(self, data):
		# returns a list of videogame ids
		response = dict()
		response['error'] = True
		response['game_ids'] = []

		user_id = int(data['user_id']) if 'user_id' in data else -1

		if user_id == -1:
			response['code'] = '2009'
		else:
			games = self.LIBRARY_DB.get_games(user_id)
			response['error'] = False
			if games:
				response['game_ids'] = games
				response['code'] = '4002'
			else:
				response['code'] = '4001'
		return response

	def add_game(self, data):
		response = dict()
		response['error'] = True

		user_id = int(data['user_id']) if 'user_id' in data else -1
		game_id = int(data['game_id']) if 'game_id' in data else -1

		if user_id == -1:
			response['code'] = '2009'
		elif game_id == -1:
			response['code'] = '4003'
		else:
			self.LIBRARY_DB.add_game(user_id, game_id)
			response['code'] = '4004'
			response['error'] = False
		return response

	def check_game(self, data):
		response = dict()
		response['error'] = True

		user_id = int(data['user_id']) if 'user_id' in data else -1
		game_id = int(data['game_id']) if 'game_id' in data else -1

		if user_id == -1:
			response['code'] = '2009'
		elif game_id == -1:
			response['code'] = '4003'
		else:
			game_exists = self.LIBRARY_DB.check_game(user_id, game_id)
			response['exists'] = game_exists
			response['code'] = '4006'
			response['error'] = False
		return response

	def game_deleted(self, id):
		response = dict()
		response['error'] = True
		if not id:
			response['code'] = '4003'
		else:
			self.LIBRARY_DB.game_deleted(id)
			response['error'] = False
			response['code'] = '4004'
		return response