from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor no ar!"

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json(silent=True) or {}
    pergunta = dados.get("pergunta", "")
    return jsonify({"resposta": "Você disse: " + pergunta})
