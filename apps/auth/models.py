from sqlalchemy import Column, Integer, String
from main.settings import DB

__all__ = ['User']


class User(DB.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, index=True)

    def __repr__(self):
        return self.email

    def to_dict(self):
        return {c: getattr(self, c) for c in self._column_name_map}
