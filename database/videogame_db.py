import json


class VideogameDB:

	def __init__(self):
		self.videogames = []

	def add(self, videogame):
		self.videogames.append(videogame)

	def get_videogames(self, res_format):
		if res_format == 'json':
			return json.dumps([videogame.dump() for videogame in self.videogames])
		else:
			return self.videogames

	def get_videogame_by_id(self, id):
		videogame = False
		for u in self.videogames:
			if u.id == id:
				videogame = u
				break
		return videogame

	def get_next_id(self):
		self.sort()
		if len(self.videogames) == 0:
			return 1
		return self.videogames[-1].id + 1

	def update_videogame(self, id, name, year, price,
                 category1, category2, category3,
                 picture, banner, description):
		for v in self.videogames:
			if v.id == id:
				v.name = name
				v.year = year
				v.price = price
				v.category1 = category1
				v.category2 = category2
				v.category3 = category3
				v.picture = picture
				v.banner = banner
				v.description = description
				return True
		return False

	def delete_videogame(self, id):
		for v in self.videogames:
			if v.id == id:
				self.videogames.remove(v)
				return True
		return False

	def sort(self):
		n = len(self.videogames)
		for i in range(n-1):
			flag = 0
			for j in range(n-1):
				if self.videogames[j].id > self.videogames[j+1].id:
					tmp = self.videogames[j]
					self.videogames[j] = self.videogames[j+1]
					self.videogames[j+1] = tmp
					flag = 1
			if flag == 0:
				break
