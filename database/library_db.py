

class LibraryDB:

	def __init__(self):
		self.libraries = []

	def add_game(self, user_id, game_id):
		for l in self.libraries:
			if str(user_id) in l:
				l[str(user_id)].append(int(game_id))
				return True
		self.libraries.append({str(user_id): [int(game_id)]})

	def check_game(self, user_id, game_id):
		for l in self.libraries:
			if str(user_id) in l:
				for game in l[str(user_id)]:
					if game_id == game:
						return True
				return False
		return False

	def get_games(self, user_id):
		for l in self.libraries:
			if str(user_id) in l:
				return l[str(user_id)]
		return []

	def game_deleted(self, game_id):
		for l in self.libraries:
			for key in l:
				l[key].remove(game_id)