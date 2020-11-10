from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers.user_controller import UserController
from controllers.videogame_controller import VideogameController
from controllers.library_controller import LibraryController
from controllers.comment_controller import CommentController
from api_codes import API_MESSAGES
import json

USER_CONTROLLER = UserController()
VIDEOGAME_CONTROLLER = VideogameController()
LIBRARY_CONTROLLER = LibraryController()
COMMENT_CONTROLLER = CommentController()

admin_data = {
    'id': 0,
    'username': 'admin',
    'first_name': 'Usuario',
    'last_name': 'Maestro',
    'password': 'admin',
    'user_type': 1
}
USER_CONTROLLER.create(admin_data)
user_data = {
    'username': 'edgar',
    'first_name': 'Edgar',
    'last_name': 'Guzman',
    'password': 'edgar',
}
USER_CONTROLLER.create(user_data)


dota_data = {
    'name': 'Dota 2',
    'year': '2013',
    'price': 0.0,
    'category1': 'MOBA',
    'category2': 'Multijugador',
    'category3': 'Free to play',
    'picture': 'https://www.mobygames.com/images/covers/l/604105-dota-2-linux-front-cover.jpg',
    'banner': 'https://www.getoutfox.com/assets/images/rich-content/outfox_guides_dota2_lag_banner.png',
    'description': "Dota 2 es un videojuego perteneciente al género de Arena de batalla en línea ARTS "
                   "(«estrategia de acción en tiempo real»), también conocido como MOBA, lanzado el 9 "
                   "de julio del año 2013. El juego fue desarrollado por la empresa Valve Corporation."
                   " El título fue anunciado oficialmente el 13 de octubre de 2010, en un artículo en "
                   "el sitio web Game Informer posteriormente, entró en su etapa Beta a principios "
                   "del 2011, y finalmente se lanzó al público en general a través de Steam el 9 de "
                   "julio de 2013 para Microsoft Windows, y el 18 de julio de 2013 para OS X y Linux, "
                   "el 17 de junio de 2015 Valve lanzó la beta del juego usando el nuevo motor gráfico "
                   "Source 2 [Dota 2 Reborn], cliente que será el único y definitivo poco después del "
                   "The International 2015 según el anuncio se mantuvo fiel a su predecesor, a la vez "
                   "que incrementó la calidad del producto final, además de ofrecer una experiencia "
                   "envolvente y gratificante para los jugadores. Sin embargo, Dota 2 es actualmente "
                   "criticado por tener una dura curva de aprendizaje y una comunidad de las más hostiles "
                   "en el ámbito de internet. Actualmente es el juego más jugado de Steam con más de 40.6 "
                   "millones de jugadores únicos que se conectan casi en su totalidad con frecuencia "
                   "diaria y ha llegado a ser incluido en el Guinness World Records Gamer's Edition."
}
VIDEOGAME_CONTROLLER.create(dota_data)
dbfz_data = {
    'name': 'Dragon Ball FighterZ',
    'year': '2018',
    'price': 480.50,
    'category1': 'Lucha',
    'category2': 'Multijugador',
    'category3': 'Anime',
    'picture': 'https://www.mobygames.com/images/covers/l/452367-dragon-ball-fighterz-xbox-one-front-cover.jpg',
    'banner': 'http://i2.wp.com/www.dragonball.co/wp-content/uploads/2018/07/ob_e643f4_dbfz-banner.jpg?fit=1600%2C500',
    'description': "Dragon Ball FighterZ es un videojuego de lucha en 2D desarrollado por Arc System Works "
                   "y distribuido por Bandai Namco Entertainment, basado en la franquicia Dragon Ball. "
                   "Su lanzamiento a nivel internacional se produjo el 26 de enero de 2018, mientras que en "
                   "Japón fue lanzado el 1 de febrero del mismo año, para las plataformas PlayStation 4, "
                   "Xbox One y Microsoft Windows. El juego se lanzó en la consola Nintendo Switch el 27 "
                   "de septiembre de 2018 en Japón y un día más tarde en el resto del mundo."
}
VIDEOGAME_CONTROLLER.create(dbfz_data)
valorant_data = {
    'name': 'Valorant',
    'year': '2020',
    'price': 0.0,
    'category1': 'FPS',
    'category2': 'Multijugador',
    'category3': 'Free to play',
    'picture': 'https://www.pcgamesarchive.com/wp-content/uploads/2020/06/Valorant-Cover.jpg',
    'banner': 'https://i.ytimg.com/vi/YHcP490H1J8/maxresdefault.jpg',
    'description': 'Valorant es un videojuego de disparos en primera persona multijugador '
                   'gratuito desarrollado y publicado por Riot Games. El juego se anunció '
                   'por primera vez con el nombre en clave Project A en octubre de 2019. '
                   'Fue lanzado para Microsoft Windows el 2 de junio de 2020. '
                   'Tuvo una beta cerrada que fue lanzada el 7 de abril de 2020.'
}
VIDEOGAME_CONTROLLER.create(valorant_data)
overwatch_data = {
    'name': 'Overwatch',
    'year': '2016',
    'price': 150.00,
    'category1': 'FPS',
    'category2': 'Multijugador',
    'category3': '',
    'picture': 'https://vignette1.wikia.nocookie.net/overwatch/images/9/9c/OW_SE_FOB_r4.jpg/revision/latest?cb=20151112212313',
    'banner': 'https://s1.thcdn.com/widgets/96-en/53/OVERWATCH-top-banner-012553.jpg',
    'description': 'Overwatch es un videojuego de disparos en primera persona multijugador, '
                   'desarrollado por Blizzard Entertainment. Fue lanzado al público el 24 de mayo del 2016, '
                   'para las plataformas PlayStation 4, Xbox One, Microsoft Windows y Nintendo Switch. '
                   'El juego fue anunciado el 7 de noviembre de 2014 durante la BlizzCon 2014, '
                   'y su versión beta cerrada fue estrenada el 27 de octubre de 2015. \n '
                   'Overwatch pone a los jugadores en equipos de seis personas, con cada persona escogiendo '
                   'uno de varios héroes disponibles, cada uno con movimientos y habilidades únicas. '
                   'Los héroes están divididos en tres clases: Daño, Tanque y Apoyo. Los jugadores de cada '
                   'equipo trabajan juntos para atacar y defender puntos de control o para atacar/defender '
                   '"cargas" (objetivos móviles que se mueven alrededor del mapa). Al terminar la partida '
                   'los jugadores acumulan puntos, que les otorgan recompensas estéticas que no afectan el desempeño de juego.\n '
}
VIDEOGAME_CONTROLLER.create(overwatch_data)

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    copito = "Edgar's games store backend"
    return "<H1>" + copito + "</H1>"


@app.route("/user/login", methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        res = USER_CONTROLLER.login(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/user/register", methods=['POST'])
def register_user():
    if request.method == 'POST':
        data = request.json
        res = USER_CONTROLLER.create(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/user/create", methods=['POST'])
def create_user():
    if request.method == 'POST':
        data = request.json
        res = USER_CONTROLLER.create(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/user/update", methods=['POST'])
def update_user():
    if request.method == 'POST':
        data = request.json
        res = USER_CONTROLLER.edit(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/user/get", methods=['POST'])
def get_user():
    if request.method == 'POST':
        data = request.json
        res = USER_CONTROLLER.get_user(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/user/get-all", methods=['POST'])
def get_all_users():
    if request.method == 'POST':
        data = request.json
        res = USER_CONTROLLER.get_users('json')
        return res

@app.route("/user/forgot_password", methods=['POST'])
def forgot_password():
    if request.method == 'POST':
        data = request.json
        res = USER_CONTROLLER.recover_password(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/user/games/add", methods=['POST'])
def add_user_game():
    if request.method == 'POST':
        data = request.json
        res = LIBRARY_CONTROLLER.add_game(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/user/games/get", methods=['POST'])
def get_user_games():
    if request.method == 'POST':
        data = request.json
        res = LIBRARY_CONTROLLER.get_game_ids(data)
        game_ids = res['game_ids']
        res['games_data'] = [VIDEOGAME_CONTROLLER.get_videogame({'id': id}) for id in game_ids]
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/user/games/check", methods=['POST'])
def check_videogame():
    if request.method == 'POST':
        data = request.json
        res = LIBRARY_CONTROLLER.check_game(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/videogame/create", methods=['POST'])
def create_videogame():
    if request.method == 'POST':
        data = request.json
        res = VIDEOGAME_CONTROLLER.create(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/videogame/update", methods=['POST'])
def update_videogame():
    if request.method == 'POST':
        data = request.json
        res = VIDEOGAME_CONTROLLER.edit(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/videogame/delete", methods=['POST'])
def delete_videogames():
    if request.method == 'POST':
        data = request.json
        res = VIDEOGAME_CONTROLLER.delete(data)
        res['message'] = API_MESSAGES[res['code']]
        if not res['error']:
            del_from_libraries = LIBRARY_CONTROLLER.game_deleted(res['id'])
            res['deleted_from_libraries'] = del_from_libraries
            res['deleted_from_libraries']['message'] = API_MESSAGES[del_from_libraries['code']]
        return res

@app.route("/videogame/get", methods=['POST'])
def get_videogame():
    if request.method == 'POST':
        data = request.json
        res = VIDEOGAME_CONTROLLER.get_videogame(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/videogame/get-all", methods=['POST'])
def get_videogames():
    if request.method == 'POST':
        data = request.json
        res = VIDEOGAME_CONTROLLER.get_videogames('json')
        return res

@app.route("/videogame/category/find", methods=['POST'])
def find_videogames():
    if request.method == 'POST':
        data = request.json
        res = VIDEOGAME_CONTROLLER.find(data)
        return res

@app.route("/videogame/comment/add", methods=['POST'])
def add_comment():
    if request.method == 'POST':
        data = request.json
        res = COMMENT_CONTROLLER.create(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

@app.route("/videogame/comment/get", methods=['POST'])
def get_comments():
    if request.method == 'POST':
        data = request.json
        res = COMMENT_CONTROLLER.get_comments_by_game(data)
        res['message'] = API_MESSAGES[res['code']]
        return res

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
