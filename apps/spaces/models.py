import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Text, DateTime, Numeric, JSON

from main.settings import DB

__all__ = ['Venue', 'Space', 'SpaceImage', 'Feature', 'SpaceFeature', 'Order', 'OrderItem']


class Venue(DB.Model):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Space(DB.Model):
    __tablename__ = 'spaces'

    id = Column(Integer, primary_key=True)
    venue_id = Column(Integer, None, ForeignKey('venues.id'))
    owner_id = Column(Integer, None, ForeignKey('users.id'))

    name = Column(String(100))


class SpaceImage(DB.Model):
    __tablename__ = 'space_images'

    id = Column(Integer, primary_key=True)
    space_id = Column(Integer, None, ForeignKey('spaces.id'))
    file = Column(String(300))
    order = Column(SmallInteger, default=0)


class Feature(DB.Model):
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    description = Column(Text())


class SpaceFeature(DB.Model):
    __tablename__ = 'space_features'

    id = Column(Integer, primary_key=True)
    space_id = Column(Integer, None, ForeignKey('spaces.id'))
    feature_id = Column(Integer, None, ForeignKey('features.id'))
    price = Column(Numeric, default=0)


class Order(DB.Model):
    __tablename__ = 'orders'

    NEW, APPROVED, PAID, UNPAID, WAITING = 'NEW', 'APPROVED', 'PAID', 'UNPAID', 'WAITING'

    id = Column(Integer, primary_key=True)
    space_id = Column(Integer, None, ForeignKey('spaces.id'))
    user_id = Column(Integer, None, ForeignKey('users.id'))
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(8), default=NEW, index=True)

    # these fields can be changed by vendor so we will store this data in format:
    # {'booked': 'VALUE', 'new': 'NEW_VALUE'} or without key 'new' {'booked': 'VALUE'}
    activity_type = Column(JSON)
    configuration = Column(JSON)
    booking_date_start = Column(JSON)
    booking_date_end = Column(JSON)


class OrderItem(DB.Model):
    __tablename__ = 'order_items'

    PAID, UNPAID, REFUNDED = 'PAID', 'UNPAID', 'REFUNDED'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, None, ForeignKey('orders.id'))
    feature_id = Column(Integer, None, ForeignKey('space_features.id'), nullable=True)
    price = Column(Numeric, default=0)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(8), default=PAID)
    name = Column(String(100), default='')
