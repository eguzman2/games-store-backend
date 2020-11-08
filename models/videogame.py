class Videogame:
    def __init__(self, id, name, year, price,
                 category1, category2, category3,
                 picture, banner, description):
        self.id = id
        self.name = name
        self.year = year
        self.price = price
        self.category1 = category1
        self.category2 = category2
        self.category3 = category3
        self.picture = picture
        self.banner = banner
        self.description = description

    def dump(self):
        data = {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'price': self.price,
            'category1': self.category1,
            'category2': self.category2,
            'category3': self.category3,
            'picture': self.picture,
            'banner': self.banner,
            'description': self.description
        }
        return data
