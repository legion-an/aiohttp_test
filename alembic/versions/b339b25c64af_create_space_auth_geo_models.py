"""create space, auth, geo models

Revision ID: b339b25c64af
Revises: 
Create Date: 2019-03-26 18:22:32.935052

"""
import datetime

from alembic import op
from sqlalchemy import Column, Integer, String, ColumnDefault, SmallInteger, JSON, ForeignKey, Numeric, DateTime, Text


# revision identifiers, used by Alembic.
revision='b339b25c64af'
down_revision=None
branch_labels=None
depends_on=None


def upgrade():
    op.create_table(
        'regions',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('name', String(length=50))
    )
    op.create_table(
        'cities',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('name', String(length=50), default=ColumnDefault('')),
        Column('region_id', Integer(), ForeignKey('regions.id')),
        Column('image', String(length=300))
    )
    op.create_table(
        'users',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('email', String(length=50))
    )
    op.create_table(
        'venues',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('name', String(length=100))
    )
    op.create_table(
        'spaces',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('venue_id', Integer(), ForeignKey('venues.id')),
        Column('owner_id', Integer(), ForeignKey('users.id')),
        Column('name', String(length=100))
    )
    op.create_table(
        'space_images',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('space_id', Integer(), ForeignKey('spaces.id')),
        Column('file', String(length=300)),
        Column('order', SmallInteger(), default=ColumnDefault(0))
    )
    op.create_table(
        'features',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('name', String(length=40)),
        Column('description', Text())
    )
    op.create_table(
        'space_features',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('space_id', Integer(), ForeignKey('spaces.id')),
        Column('feature_id', Integer(), ForeignKey('features.id')),
        Column('price', Numeric(), default=ColumnDefault(0))
    )
    op.create_table(
        'orders',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('space_id', Integer(), ForeignKey('spaces.id')),
        Column('user_id', Integer(), ForeignKey('users.id')),
        Column('date_created', DateTime(), default=ColumnDefault(datetime.datetime.utcnow)),
        Column('status', String(length=8), default=ColumnDefault('NEW')),
        Column('activity_type', JSON()),
        Column('configuration', JSON()),
        Column('booking_date_start', JSON()),
        Column('booking_date_end', JSON())
    )
    op.create_table(
        'order_items',
        Column('id', Integer(), primary_key=True, nullable=False),
        Column('order_id', Integer(), ForeignKey('orders.id')),
        Column('feature_id', Integer(), ForeignKey('space_features.id')),
        Column('price', Numeric(), default=ColumnDefault(0)),
        Column('date_created', DateTime(), default=ColumnDefault(datetime.datetime.utcnow)),
        Column('status', String(length=8), default=ColumnDefault('PAID')),
        Column('name', String(length=100), default=ColumnDefault(''))
    )


def downgrade():
    tables = ('order_items', 'orders', 'space_features', 'space_images', 'cities', 'regions', 'spaces',
              'users', 'venues', 'features')
    for t in tables:
        op.drop_table(t)
