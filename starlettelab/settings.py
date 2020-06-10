from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
EXCEPTION_SECRET = config("EXCEPTION_SECRET", cast=Secret)
