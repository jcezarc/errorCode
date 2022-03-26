from api import divisao, conexao, carrega, obj_dict

dados = [
    divisao(5, 0),
    divisao(7, 3),
    carrega('arquivo.txt'),
    carrega('errors.py'),
    obj_dict(
        conexao(user='root', password='***')
    ),
]
print(dados)
