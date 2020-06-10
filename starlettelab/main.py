from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Route

from .middleware import FooMiddleware
from .routes import exception, hello, home
from .settings import DEBUG

routes = [
    Route("/", home),
    Route("/hello/{name}", hello),
    Route("/exception/{secret}", exception),
]

application = Starlette(
    debug=DEBUG, routes=routes, middleware=[Middleware(FooMiddleware)]
)
