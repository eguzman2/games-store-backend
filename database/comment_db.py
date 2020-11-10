import json


class CommentDB:

	def __init__(self):
		self.comments = []

	def add(self, comment):
		self.comments.append(comment)

	def get_comments(self, res_format):
		if res_format == 'json':
			return json.dumps([c.dump() for c in self.comments])
		else:
			return self.comments

	def get_comments_by_game(self, game_id):
		comments_list = []
		for c in self.comments:
			if c.game_id == int(game_id):
				comments_list.append(c)
		return comments_list

	def get_next_id(self):
		self.sort()
		if len(self.comments) == 0:
			return 1
		return self.comments[-1].id + 1

	def sort(self):
		n = len(self.comments)
		for i in range(n-1):
			flag = 0
			for j in range(n-1):
				if self.comments[j].id > self.comments[j+1].id:
					tmp = self.comments[j]
					self.comments[j] = self.comments[j+1]
					self.comments[j+1] = tmp
					flag = 1
			if flag == 0:
				break
