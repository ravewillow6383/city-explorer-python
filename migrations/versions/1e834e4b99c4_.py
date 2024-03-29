"""empty message

Revision ID: 1e834e4b99c4
Revises: 
Create Date: 2019-07-23 18:00:35.303034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e834e4b99c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('formatted_query', sa.String(length=1024), nullable=True),
    sa.Column('search_query', sa.String(length=256), nullable=True),
    sa.Column('latitude', sa.Float(precision=10.7), nullable=True),
    sa.Column('longitude', sa.Float(precision=10.7), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('search_query')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location_model')
    # ### end Alembic commands ###
