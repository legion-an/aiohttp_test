"""add spaces models

Revision ID: 1fa8a46d2e2b
Revises: bb26e545d0b0
Create Date: 2019-03-22 19:08:26.314534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fa8a46d2e2b'
down_revision = 'bb26e545d0b0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'spaces',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('users.id'))
    )
    op.create_table(
        'space_images',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('file', sa.String(300)),
        sa.Column('space_id', sa.Integer, sa.ForeignKey('regions.id')),
        sa.Column('order', sa.SmallInteger, default=0),
    )
    op.create_table(
        'features',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('description', sa.Text())
    )
    op.create_table(
        'space_features',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('space_id', sa.Integer, sa.ForeignKey('spaces.id')),
        sa.Column('feature_id', sa.Integer, sa.ForeignKey('features.id'))
    )


def downgrade():
    for t in ('space_features', 'space_images', 'features', 'spaces'):
        op.drop_table(t)
