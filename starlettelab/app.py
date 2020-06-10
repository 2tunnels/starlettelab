from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Route

from .middleware import FooMiddleware
from .routes import hello, home

routes = [
    Route("/", home),
    Route("/hello/{name}", hello),
]

application = Starlette(routes=routes, middleware=[Middleware(FooMiddleware)])
