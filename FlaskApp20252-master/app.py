from flask import Flask, request, jsonify

from models.Usuario import Usuario  
from helpers.data import getInstituicoesEnsino  # Função para carregar instituições de ensino
from models.InstituicaoEnsino import InstituicaoEnsino  # Importa o modelo InstituicaoEnsino

# Criação da aplicação Flask
app = Flask(__name__)

# Criação de um usuário inicial para teste
usuario = Usuario(1, "João", "00011122233", "2025-10-09")
usuarios = [usuario]  # Lista inicial de usuários

# Carregamento das instituições de ensino a partir dos dados
instituicoesEnsino = getInstituicoesEnsino()

# Rota principal para verificar a versão da API
@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200

# Rota para listar todos os usuários
@app.get("/usuarios")
def getUsuarios():
    return jsonify(usuarios)

# Rota para obter um usuário específico pelo ID
@app.get("/usuarios/<int:id>")
def getUsuariosById(id: int):
    return jsonify(usuarios[id])

# Rota para criar um novo usuário
@app.post("/usuarios")
def createUsuario():
    data = request.get_json()  # Obtém os dados enviados no corpo da requisição
    novo_usuario = Usuario(
        id=len(usuarios),  # Define o ID como o próximo na lista
        nome=data.get("nome"),
        cpf=data.get("cpf"),
        nascimento=data.get("nascimento")
    )
    usuarios.append(novo_usuario)  # Adiciona o novo usuário à lista
    return jsonify(novo_usuario.to_json()), 201  # Retorna o usuário criado com status 201

# Rota para listar todas as instituições de ensino
@app.get("/instituicoesensino")
def getInstituicoesEnsino():
    # Converte as instituições para JSON antes de retornar
    instituicoesEnsinoJson = [instituicaoEnsino.to_json()
                              for instituicaoEnsino in instituicoesEnsino]
    return jsonify(instituicoesEnsinoJson), 200

# Rota para obter uma instituição específica pelo ID
@app.get("/instituicoesensino/<int:id>")
def getInstituicoesEnsinoById(id: int):
    ieDict = instituicoesEnsino[id].to_json()  # Converte a instituição para JSON
    return jsonify(ieDict), 200

# Rota para obter um atributo específico de um usuário
@app.get("/usuarios/<int:id>/<string:key>")
def getUsuarioAttribute(id: int, key: str):
    return jsonify(usuarios[id].get(key)), 200

# Rota para obter um atributo específico de uma instituição de ensino
@app.get("/instituicoesensino/<int:id>/<string:key>")
def getInstituicaoEnsinoAttribute(id: int, key: str):
    return jsonify(instituicoesEnsino[id].get(key)), 200

# Rota para criar uma nova instituição de ensino
@app.post("/instituicoesensino")
def createInstituicaoEnsino():
    data = request.get_json()  # Obtém os dados enviados no corpo da requisição
    nova_instituicao = InstituicaoEnsino(
        codigo=len(instituicoesEnsino),  # Define o código como o próximo na lista
        nome=data.get("nome"),
        co_uf=data.get("co_uf"),
        co_municipio=data.get("co_municipio"),
        qt_mat_bas=data.get("qt_mat_bas"),
        qt_mat_prof=data.get("qt_mat_prof"),
        qt_mat_eja=data.get("qt_mat_eja"),
        qt_mat_esp=data.get("qt_mat_esp")
    )
    instituicoesEnsino.append(nova_instituicao)  # Adiciona a nova instituição à lista
    return jsonify(nova_instituicao.to_json()), 201  # Retorna a instituição criada com status 201

# todo: entregar endpoints completos de IE e Usuarios.
