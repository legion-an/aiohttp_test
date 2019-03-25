import json
from json import JSONDecodeError

from aiohttp import web
from asyncpg import UniqueViolationError
from schematics.exceptions import DataError
from schematics.models import Model
from schematics.types import EmailType

from apps.auth.models import User
from utils.misc import BaseView


class UserSchema(Model):
    email = EmailType(required=True)


class UserView(BaseView):

    async def get(self):
        users = await User.query.gino.all()
        data = [user.to_dict() for user in users]
        return web.json_response(data)

    async def post(self):
        data = await self.request.text()
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
