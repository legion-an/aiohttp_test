from apps.geo.views import IndexView
from apps.auth.views import create_user, users_list


def setup_routes(app):
    app.router.add_route('GET', '/', IndexView)
    app.router.add_route('GET', '/users/', users_list)
    app.router.add_route('POST', '/users/create/', create_user)
