"""add user model

Revision ID: bb26e545d0b0
Revises: a47fa14d3f7b
Create Date: 2019-03-22 19:08:18.765858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb26e545d0b0'
down_revision = 'a47fa14d3f7b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), unique=True, index=True),
    )


def downgrade():
    op.drop_table('users')
