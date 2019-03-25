from apps.geo.views import IndexView
from apps.auth.views import UserView


def setup_routes(app):
    app.router.add_view('/', IndexView)
    app.router.add_view('/users/', UserView)
