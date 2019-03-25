import asyncio

import aiohttp_debugtoolbar
import uvloop
from aiohttp_swagger import *
from aiohttp import web
from aiohttp_jwt import JWTMiddleware

from main import settings

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def init_app(app):
    # add routes
    from main.routes import setup_routes

    setup_routes(app)

    if settings.DEBUG:
        setup_swagger(app, swagger_url='/docs')


async def close_app(app):
    pass


app = web.Application(
    middlewares=[
        settings.DB,
        JWTMiddleware(settings.SHARED_SECRET_KEY, credentials_required=False)
    ]
)

app['settings'] = settings
app.on_startup.append(init_app)
app.on_cleanup.append(close_app)

settings.DB.init_app(app, config=settings.DATABASE)


# enable debugtoolbar
if settings.DEBUG:
    aiohttp_debugtoolbar.setup(app)


if __name__ == '__main__':
    web.run_app(app, host=settings.HOST, port=settings.PORT)
