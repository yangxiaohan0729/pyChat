from flask import Flask, Response
from flask_socketio import SocketIO
import os.path

from src import osPaths

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

clients = []
clientNicknames = []

# returning of actual pages


@app.route("/", methods=["GET"])
def signInPage():
    return osPaths.getFile("/client/signIn.html")


@app.route("/chat")
def chatPage():
    return osPaths.getFile("/client/index.html")


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)

# # returning of resource pages
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def get_resource(path):  # pragma: no cover
#     mimetypes = {
#         ".css": "client/css/stylesheet",
#         ".html": "client/index",
#         ".js": "client/javascript/javascript",
#     }
#     complete_path = os.path.join(osPaths.rootDir(), path)
#     print(osPaths.rootDir())
#     print(path)
#     ext = os.path.splitext(path)[1]
#     mimetype = mimetypes.get(ext, "client/index")
#     content = osPaths.getFile(path)
#     return Response(content, mimetype=mimetype)


osPaths.check()
