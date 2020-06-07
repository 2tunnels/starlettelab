from starlette.requests import Request
from starlette.responses import JSONResponse


def home(request: Request) -> JSONResponse:
    return JSONResponse({"message": "Hello world!"})
