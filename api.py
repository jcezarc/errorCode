import mysql.connector
import errors

def set_error(error_code: str):
    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return {
                    'error_code': error_code,
                    'exception': type(e).__name__,
                    'function': func.__name__
                }
        return wrapper
    return decorator


@set_error(errors.ERRO_DE_CALCULO)
def divisao(a: int, b: int) -> int:
    return a / b

@set_error(errors.ERRO_BANCO_DADOS)
def conexao(**args) -> mysql.connector.connection.MySQLConnection:
    return mysql.connector.connect(**args)

@set_error(errors.ERRO_ARQUIVO_NAO_ENCONTRADO)
def carrega(arquivo: str):
    with open(arquivo) as f:
        return f.read()

@set_error(errors.ERRO_OBJETO_NONE)
def obj_dict(obj: object()) -> dict:
    return obj.__dict__
