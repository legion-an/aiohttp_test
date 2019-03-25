from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Text
from server import db


class Space(db.Model):
    __tablename__ = 'spaces'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    owner_id = Column(Integer, None, ForeignKey('users.id'))


class SpaceImage(db.Model):
    __tablename__ = 'space_images'

    id = Column(Integer, primary_key=True)
    space_id = Column(Integer, None, ForeignKey('spaces.id'))
    file = Column(String(300))
    order = Column(SmallInteger, default=0)


class Feature(db.Model):
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    description = Column(Text())


class SpaceFeature(db.Model):
    __tablename__ = 'space_features'

    id = Column(Integer, primary_key=True)
    space_id = Column(Integer, None, ForeignKey('spaces.id'))
    feature_id = Column(Integer, None, ForeignKey('features.id'))
