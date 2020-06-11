from starlette.config import environ

environ["DEBUG"] = "False"
environ["EXCEPTION_SECRET"] = "swordfish"
environ["BUGSNAG_API_KEY"] = "secret"
