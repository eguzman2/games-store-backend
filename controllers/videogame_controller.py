from models.videogame import Videogame
from database.videogame_db import VideogameDB
import json


class VideogameController:

	def __init__(self):
		self.VIDEOGAME_DB = VideogameDB()

	def get_videogames(self, res_format='list'):
		return self.VIDEOGAME_DB.get_videogames(res_format)

	def get_videogame(self, data):
		response = dict()
		response['error'] = True

		id = int(data['id']) if 'id' in data else -1

		if id == -1:
			response['code'] = '3001'
		else:
			videogame = self.VIDEOGAME_DB.get_videogame_by_id(id)
			if videogame:
				response.update(videogame.dump())
				response['code'] = '3002'
				response['error'] = False
			else:
				response['code'] = '3003'

		return response

	def find(self, data):
		response = dict()
		response['error'] = True

		search_text = data['search_text'] if 'search_text' in data else ""

		if search_text == "":
			response['code'] = '3008'
		else:
			videogames = self.VIDEOGAME_DB.search(search_text)
			if videogames:
				response = json.dumps([videogame.dump() for videogame in videogames])
				# response['code'] = '3010'
				# response['error'] = False
				print(response)
			else:
				response['code'] = '3009'
		return response

	def create(self, data):
		response = dict()
		response['error'] = True

		id = self.VIDEOGAME_DB.get_next_id() if 'id' not in data else data['id']

		name = data['name'] if 'name' in data else ''
		year = data['year'] if 'year' in data else ''
		price = data['price'] if 'price' in data else ''
		category1 = data['category1'] if 'category1' in data else ''
		category2 = data['category2'] if 'category2' in data else ''
		category3 = data['category3'] if 'category3' in data else ''
		picture = data['picture'] if 'picture' in data else ''
		banner = data['banner'] if 'banner' in data else ''
		description = data['description'] if 'description' in data else ''

		new_videogame = Videogame(id, name, year, price, category1,
								  category2, category3, picture,
								  banner, description)
		self.VIDEOGAME_DB.add(new_videogame)
		response['code'] = '3004'
		response.update(new_videogame.dump())
		response['error'] = False
		return response

	def edit(self, data):
		response = dict()
		response['error'] = True

		id = int(data['id']) if 'id' in data else -1
		name = data['name'] if 'name' in data else ''
		year = data['year'] if 'year' in data else ''
		price = data['price'] if 'price' in data else ''
		category1 = data['category1'] if 'category1' in data else ''
		category2 = data['category2'] if 'category2' in data else ''
		category3 = data['category3'] if 'category3' in data else ''
		picture = data['picture'] if 'picture' in data else ''
		banner = data['banner'] if 'banner' in data else ''
		description = data['description'] if 'description' in data else ''

		if id == -1:
			response['code'] = '3005'
		else:
			updated = self.VIDEOGAME_DB.update_videogame(id, name, year, price, category1,
														 category2, category3, picture,
														 banner, description)
			if updated:
				response['code'] = '3006'
				response['error'] = False
			else:
				response['code'] = '3003'

		return response

	def delete(self, data):
		response = dict()
		response['error'] = True

		id = int(data['id']) if 'id' in data else -1

		if id == -1:
			response['code'] = '3001'
		else:
			deleted = self.VIDEOGAME_DB.delete_videogame(id)

			if deleted:
				response['error'] = False
				response['code'] = '3007'
				response['id'] = id
			else:
				response['code'] = '3003'

		return response
