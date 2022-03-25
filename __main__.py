from api import divisao, conexao, carrega_arquivo, dados_do_obj

dados = [
    divisao(5, 0),
    conexao(user='root', password='***'),
    carrega_arquivo('arquivo.txt'),
    dados_do_obj(None),
]
print(dados)
