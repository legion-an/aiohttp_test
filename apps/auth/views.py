import json
from json import JSONDecodeError

from aiohttp import web
from asyncpg import UniqueViolationError
from schematics.exceptions import DataError
from schematics.models import Model
from schematics.types import EmailType

from apps.auth.models import User


class UserSchema(Model):
    email = EmailType(required=True)


async def users_list(request):
    """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - Health check
        produces:
        - text/plain
        responses:
            "200":
                description: successful operation. Return "pong" text
            "405":
                description: invalid HTTP Method
        """
    users = await User.query.gino.all()
    data = [user.to_dict() for user in users]
    return web.json_response(data)


async def create_user(request):
    """
        ---
        description: This end-point allow to test that service is up.
    """

    data = await request.text()
    try:
        schema = UserSchema(json.loads(data))
        schema.validate()
    except DataError as err:
        return web.json_response({'details': err.to_primitive()}, status=400)
    except JSONDecodeError:
        return web.json_response({'details': 'Decode error'}, status=400)

    validated_data = schema.to_primitive()
    try:
        user = await User.create(**validated_data)
    except UniqueViolationError:
        return web.json_response({'details': 'This email is already in use'}, status=400)
    return web.json_response(user.to_dict())
