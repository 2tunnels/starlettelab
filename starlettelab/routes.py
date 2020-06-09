from starlette.requests import Request
from starlette.responses import JSONResponse


def home(request: Request) -> JSONResponse:
    return JSONResponse({"message": "Hello world!"})


def hello(request: Request) -> JSONResponse:
    name = request.path_params["name"]

    if name == "jon":
        message = "You know nothing, Jon Snow"
    else:
        message = f"Hello, {name}!"

    return JSONResponse({"message": message})
