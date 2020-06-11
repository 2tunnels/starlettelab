import random

from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_403_FORBIDDEN

from . import __version__
from .settings import EXCEPTION_SECRET


async def home(request: Request) -> JSONResponse:
    return JSONResponse({"message": "Hello world!"})


async def health(request: Request) -> JSONResponse:
    return JSONResponse({"version": __version__})


async def hello(request: Request) -> JSONResponse:
    name = request.path_params["name"]

    if name == "jon":
        message = "You know nothing, Jon Snow"
    else:
        message = f"Hello, {name}!"

    return JSONResponse({"message": message})


async def exception(request: Request) -> JSONResponse:
    """Route for testing error logging, monitoring and reporting."""

    secret = request.path_params["secret"]
    random_number = random.random()  # noqa

    if secret == str(EXCEPTION_SECRET):
        raise RuntimeError("You guessed the secret!")

    return JSONResponse({"error": "Wrong secret"}, status_code=HTTP_403_FORBIDDEN)
