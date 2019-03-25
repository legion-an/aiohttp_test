from aiohttp import web

from utils.misc import BaseView


class IndexView(BaseView):

    async def get(self):
        return web.Response(text='INDEX')

    async def post(self):
        return web.Response(text='POST')

