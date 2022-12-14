"""empty message

Revision ID: 9c13a1872a03
Revises: 7663bc72a775
Create Date: 2022-09-13 16:30:47.766560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c13a1872a03'
down_revision = '7663bc72a775'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contribution')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contribution',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('amount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('charity_id2', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='contribution_user_id_fkey')
    )
    # ### end Alembic commands ###
