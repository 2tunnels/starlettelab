from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_403_FORBIDDEN

from .settings import EXCEPTION_SECRET


async def home(request: Request) -> JSONResponse:
    return JSONResponse({"message": "Hello world!"})


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

    if secret == str(EXCEPTION_SECRET):
        raise RuntimeError("You guessed the secret!")

    return JSONResponse({"error": "Wrong secret"}, status_code=HTTP_403_FORBIDDEN)
