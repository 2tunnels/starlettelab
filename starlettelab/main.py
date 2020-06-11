from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Route
from starlette_x_bugsnag.middleware import BugsnagMiddleware

from . import __version__
from .middleware import FooMiddleware
from .routes import exception, health, hello, home
from .settings import BUGSNAG_API_KEY, DEBUG

routes = [
    Route("/", home),
    Route("/health", health),
    Route("/hello/{name}", hello),
    Route("/exception/{secret}", exception),
]

release_stage = "development" if DEBUG else "production"

application = Starlette(
    debug=DEBUG,
    routes=routes,
    middleware=[
        Middleware(FooMiddleware),
        Middleware(
            BugsnagMiddleware,
            api_key=str(BUGSNAG_API_KEY),
            app_version=__version__,
            project_root=None,
            release_stage=release_stage,
        ),
    ],
)
