# Importa o módulo JSON para manipulação de arquivos JSON
import json
from models.InstituicaoEnsino import InstituicaoEnsino  # Importa o modelo InstituicaoEnsino

# Função para carregar as instituições de ensino a partir de um arquivo JSON
def getInstituicoesEnsino():

    instituicoesEnsino = []  # Lista para armazenar as instituições de ensino

    # Lê o arquivo JSON contendo os dados das instituições de ensino
    with open('data/instituicoesensino.json', 'r') as f:
        instituicoesEnsinoJson = json.load(f)

    # Converte os dados JSON para objetos da classe InstituicaoEnsino
    for instituicaoEnsinoJson in instituicoesEnsinoJson:
        ie = InstituicaoEnsino(instituicaoEnsinoJson["codigo"],
                               instituicaoEnsinoJson["nome"],
                               instituicaoEnsinoJson["co_uf"],
                               instituicaoEnsinoJson["co_municipio"],
                               instituicaoEnsinoJson["qt_mat_bas"],
                               instituicaoEnsinoJson["qt_mat_prof"],
                                0,  # Valor padrão para qt_mat_eja
                               instituicaoEnsinoJson["qt_mat_esp"])
        instituicoesEnsino.append(ie)  # Adiciona a instituição à lista

    return instituicoesEnsino  # Retorna a lista de instituições de ensino

# Chamada inicial para carregar as instituições de ensino
getInstituicoesEnsino()
