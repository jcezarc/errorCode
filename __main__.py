from api import divisao, conexao, carrega, obj_dict

dados = [
    divisao(5, 0),
    conexao(user='root', password='***'),
    carrega('arquivo.txt'),
    obj_dict(None),
]
print(dados)
