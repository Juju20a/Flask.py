from flask import Flask, request, jsonify, abort
from models.Usuario import Usuario
from models.InstituicaoEnsino import InstituicaoEnsino
from helpers.data import getInstituicoesEnsino
import json
import os

app = Flask(__name__)

# Caminhos dos arquivos de dados
DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "usuarios.json")
INSTIT_FILE = os.path.join(DATA_DIR, "instituicoes.json")

# Garante que a pasta exista
os.makedirs(DATA_DIR, exist_ok=True)

# Funções utilitárias de leitura e escrita JSON
def read_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# --- Inicialização de dados ---
usuarios = read_json(USERS_FILE)
instituicoesEnsino = read_json(INSTIT_FILE)

# Rota principal
@app.get("/")
def index():
    return jsonify({"versao": "2.0.0"}), 200



@app.get("/usuarios")
def getUsuarios():
    return jsonify(usuarios), 200

@app.get("/usuarios/<int:id>")
def getUsuarioById(id):
    for u in usuarios:
        if u["id"] == id:
            return jsonify(u), 200
    abort(404, "Usuário não encontrado")

@app.post("/usuarios")
def createUsuario():
    data = request.get_json()
    if not data or "nome" not in data or "cpf" not in data:
        abort(400, "Campos obrigatórios: nome e cpf")

    new_id = max([u["id"] for u in usuarios], default=0) + 1
    novo_usuario = {
        "id": new_id,
        "nome": data["nome"],
        "cpf": data["cpf"],
        "nascimento": data.get("nascimento")
    }
    usuarios.append(novo_usuario)
    write_json(USERS_FILE, usuarios)
    return jsonify(novo_usuario), 201

@app.put("/usuarios/<int:id>")
def updateUsuario(id):
    data = request.get_json()
    for i, u in enumerate(usuarios):
        if u["id"] == id:
            usuarios[i].update(data)
            write_json(USERS_FILE, usuarios)
            return jsonify(usuarios[i]), 200
    abort(404, "Usuário não encontrado")

@app.delete("/usuarios/<int:id>")
def deleteUsuario(id):
    global usuarios
    novos = [u for u in usuarios if u["id"] != id]
    if len(novos) == len(usuarios):
        abort(404, "Usuário não encontrado")
    usuarios = novos
    write_json(USERS_FILE, usuarios)
    return "", 204



@app.get("/instituicoesensino")
def getInstituicoesEnsinoRoute():
    return jsonify(instituicoesEnsino), 200

@app.get("/instituicoesensino/<int:id>")
def getInstituicaoById(id):
    for ie in instituicoesEnsino:
        if ie["codigo"] == id:
            return jsonify(ie), 200
    abort(404, "Instituição não encontrada")

@app.post("/instituicoesensino")
def createInstituicaoEnsino():
    data = request.get_json()
    if not data or "nome" not in data:
        abort(400, "Campo 'nome' é obrigatório")

    new_id = max([ie["codigo"] for ie in instituicoesEnsino], default=0) + 1
    nova_ie = {
        "codigo": new_id,
        "nome": data["nome"],
        "co_uf": data.get("co_uf"),
        "co_municipio": data.get("co_municipio"),
        "qt_mat_bas": data.get("qt_mat_bas"),
        "qt_mat_prof": data.get("qt_mat_prof"),
        "qt_mat_eja": data.get("qt_mat_eja"),
        "qt_mat_esp": data.get("qt_mat_esp"),
    }
    instituicoesEnsino.append(nova_ie)
    write_json(INSTIT_FILE, instituicoesEnsino)
    return jsonify(nova_ie), 201

@app.put("/instituicoesensino/<int:id>")
def updateInstituicaoEnsino(id):
    data = request.get_json()
    for i, ie in enumerate(instituicoesEnsino):
        if ie["codigo"] == id:
            instituicoesEnsino[i].update(data)
            write_json(INSTIT_FILE, instituicoesEnsino)
            return jsonify(instituicoesEnsino[i]), 200
    abort(404, "Instituição não encontrada")

@app.delete("/instituicoesensino/<int:id>")
def deleteInstituicaoEnsino(id):
    global instituicoesEnsino
    novas = [ie for ie in instituicoesEnsino if ie["codigo"] != id]
    if len(novas) == len(instituicoesEnsino):
        abort(404, "Instituição não encontrada")
    instituicoesEnsino = novas
    write_json(INSTIT_FILE, instituicoesEnsino)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True, port=5000)
