from functools import wraps
from loguru import logger
from sys import stderr

# Remove configurações padrão do Loguru (importante para evitar duplicações)
logger.remove()

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "log.log",  # Arquivo onde os logs serão salvos
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{function}:{line} | {module} | PID:{process} | {message}",
    level="INFO"
)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando a função {func.__name__} com os argumentos {args} e {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"A função {func.__name__} retornou {result}")
            return result
        except Exception as e:
            logger.error(f"Erro na função {func.__name__}: {str(e)}")
            return None
    return wrapper
