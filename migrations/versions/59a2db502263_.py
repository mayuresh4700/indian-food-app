"""empty message

Revision ID: 59a2db502263
Revises: 
Create Date: 2020-08-24 16:52:35.182771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59a2db502263'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_restaurant_name'), 'restaurant', ['name'], unique=True)
    op.create_table('rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('taste', sa.Float(), nullable=True),
    sa.Column('delivery', sa.Float(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rating')
    op.drop_index(op.f('ix_restaurant_name'), table_name='restaurant')
    op.drop_table('restaurant')
    # ### end Alembic commands ###
