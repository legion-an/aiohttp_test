"""create geo models

Revision ID: 49ebd6bb66a4
Revises: 
Create Date: 2019-03-22 18:38:12.766649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49ebd6bb66a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'regions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
    )
    op.create_table(
        'cities',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), default=''),
        sa.Column('region_id', sa.Integer, sa.ForeignKey('regions.id'))
    )


def downgrade():
    op.drop_table('cities')
    op.drop_table('regions')
