from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Route
from starlette_x_bugsnag.middleware import BugsnagMiddleware

from .middleware import FooMiddleware
from .routes import exception, hello, home
from .settings import BUGSNAG_API_KEY, DEBUG

routes = [
    Route("/", home),
    Route("/hello/{name}", hello),
    Route("/exception/{secret}", exception),
]

application = Starlette(
    debug=DEBUG,
    routes=routes,
    middleware=[
        Middleware(FooMiddleware),
        Middleware(BugsnagMiddleware, api_key=str(BUGSNAG_API_KEY)),
    ],
)
