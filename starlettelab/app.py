from starlette.applications import Starlette
from starlette.routing import Route

from .routes import hello, home

routes = [
    Route("/", home),
    Route("/hello/{name}", hello),
]

application = Starlette(routes=routes)
