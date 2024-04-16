from flask_json import FlaskJSON, as_json
from flask_cors import CORS, cross_origin
import uuid
import random
from flask import Flask, request
app = Flask(__name__)
cors = CORS(app)
json = FlaskJSON(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False
app.config['JSON_ADD_STATUS'] = False


def errors(func):

    def wrapper(*args, **kwargs):


        try:
            original_result = func(*args, **kwargs)

        except Exception as err:
            print(err)
            original_result = {"success": False,
                               "exception": {
                                "message": str(err)
                               }
                               }
        return original_result
    wrapper.__name__ = func.__name__
    return wrapper


usedPass = {'admin': 'password123',
            'lena': 'Roomster13'}
uuids = ['123']
gameId = [0]
ongoingGames = [{"id": 0,
                 "cards": [],
                 "shore": 0}]
cards = []
for color in range(4):
    for shape in range (4):
        for fill in range(4):
            for count in range(4):
                cards.append({"id" : color*64+shape*16+fill*4+count,
                              "color" : color,
                              "shape" : shape,
                              "fill" : fill,
                              "count" : count
                              })


@app.route('/user/register', methods=['GET'])
@cross_origin()
@as_json
@errors
def auth():
    # check parameters
    nickname = request.args.get('nickname')
    password = request.args.get('password')
    try:

        if (usedPass[nickname] != password):
            raise Exception()
        else:
            newUuid = uuid.uuid4()  #random token
            uuids.append(str(newUuid))
            response = {'success': True,
                        'exception': None,
                        'nickname': nickname,
                        'accessToken': newUuid}
            return response, 200
    except Exception:
        raise Exception("Nickname or password is incorrect")


@app.route('/set/room/create', methods=['GET'])
@cross_origin()
@as_json
@errors
def create():
    accessToken = request.args.get('accessToken')
    if (not accessToken in uuids):
        raise Exception("Wrong Access Token")
    newId = 0
    for i in range(len(gameId)+2):
        if not i in gameId:
            newId = i
            newcards = cards
            gameId.append(newId)
            ongoingGames.append({"id": newId, "cards": newcards, "score": 0})
            break

    response = {'success': True,
                'exception': None,
                'gameId': newId}
    return response, 200


@app.route('/set/room/list', methods=['GET'])
@cross_origin()
@as_json
@errors
def getlist():
    accessToken = request.args.get('accessToken')
    if (not accessToken in uuids):
        raise Exception("Wrong Access Token")

    response = {"games": []}
    for i in range(1, len(gameId)):
        a = dict.fromkeys(["id"], gameId[i])
        response["games"].append(a)
        print(gameId)

    return response, 200

@app.route('/set/room/enter', methods=['GET'])
@cross_origin()
@as_json
@errors
def enterGame():
    accessToken = request.args.get('accessToken')
    userId = request.args.get('gameId')
    if (not accessToken in uuids):
        raise Exception("Wrong Access Token")
    if (not int(userId) in gameId):
        raise Exception("Wrong game ID")

    response = {
        "success": True,
        "exception": None,
        "gameId": userId
        }

    return response, 200

def getById(id):
    for i in range(len(ongoingGames)):
        if ongoingGames[i]["id"] == id:
            return i
    return -1

@app.route('/set/field', methods=['GET'])
@cross_origin()
@as_json
@errors
def field():
    accessToken = request.args.get('accessToken')
    userGameId = request.args.get('gameId')
    if (not accessToken in uuids):
        raise Exception("Wrong Access Token")
    if (not int(userGameId) in gameId):
        raise Exception("Wrong game ID")

    response = { "cards": [],
                 "status": "ongoing",
                 "score": ongoingGames[getById(gameId)]["score"]
                 }
    for i in range(9):
        rand = random.randint(0, len(cards) - 1)
        response["cards"].append(ongoingGames[getById(gameId)]["cards"][rand])
        ongoingGames[getById(gameId)]["cards"].pop(rand)

    return response, 200

@app.route('/set/pick', methods=['GET'])
@cross_origin()
@as_json
@errors
def pick():
    accessToken = request.args.get('accessToken')
    userGameId = request.args.get('gameId')
    userCards = request.args.get('cards')
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
