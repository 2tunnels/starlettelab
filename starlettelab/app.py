from starlette.applications import Starlette
from starlette.routing import Route

from .routes import home

routes = [
    Route("/", home),
]

application = Starlette(routes=routes)
