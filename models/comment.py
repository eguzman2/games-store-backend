
class Comment:
	def __init__(self, id, game_id, username, comment):
		self.id = id
		self.game_id = game_id
		self.username = username
		self.comment = comment

	def dump(self):
		data = {
			'id': self.id,
			'game_id': self.game_id,
			'username': self.username,
			'comment': self.comment
		}
		return data