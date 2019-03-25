from aiohttp import web


class BaseView(web.View):
    """
    If you want to use Class Based View you need to use this class
    because of this bug https://github.com/aio-libs/aiohttp-debugtoolbar/issues/207
    When it will be fixed you can remove this class
    """

    def __iter__(self):
        return self._iter().__await__()
