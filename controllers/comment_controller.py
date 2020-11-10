from models.comment import Comment
from database.comment_db import CommentDB


class CommentController:
	
	def __init__(self):
		self.COMMENT_DB = CommentDB()

	def create(self, data):
		response = dict()
		response['error'] = True

		id = self.COMMENT_DB.get_next_id() if not 'id' in data else data['id']
		game_id = int(data['game_id']) if 'game_id' in data else -1
		username = data['username'] if 'username' in data else ''
		comment = data['comment'] if 'comment' in data else ''

		if game_id == -1:
			response['code'] = '4003'
		else:
			new_comment = Comment(id, game_id, username, comment)
			self.COMMENT_DB.add(new_comment)
			response['code'] = '5001'
			response.update(new_comment.dump())
			response['error'] = False
		return response

	def get_comments_by_game(self, data):
		response = dict()
		response['error'] = True
		response['comments'] = []

		game_id = int(data['game_id']) if 'game_id' in data else -1

		if game_id == -1:
			response['code'] = '4003'
		else:
			comments = self.COMMENT_DB.get_comments_by_game(game_id)
			response['error'] = False
			if comments:
				response['comments'] = [c.dump() for c in comments]
				response['code'] = '5002'
			else:
				response['code'] = '5003'
		return response