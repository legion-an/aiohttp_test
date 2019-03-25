"""add image to cities

Revision ID: a47fa14d3f7b
Revises: 49ebd6bb66a4
Create Date: 2019-03-22 18:54:44.655814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a47fa14d3f7b'
down_revision = '49ebd6bb66a4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('cities', sa.Column('image', sa.String(300)))


def downgrade():
    op.drop_column('cities', 'image')
