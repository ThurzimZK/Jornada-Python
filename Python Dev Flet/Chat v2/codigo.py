# pip install flask python-socketio flask-socketio simple-websocket

from flask import Flask, render_template 
from flask_socketio import SocketIO, send 

app = Flask(__name__) 
app.config["SECRET"] = "çççDFANasnffn5345u13!@#$!@#dfiasdcdA@$3fadf"
app.config["DEBUG"] = True 
sockteio = SocketIO(app, cors_allowed_origins='*')

@sockteio.on("message")
def gerenciar_mensagens(mensagem):
    print(f'Mensagem: {mensagem}')
    send(mensagem, broadcast=True)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    sockteio.run(app, host="localhost")