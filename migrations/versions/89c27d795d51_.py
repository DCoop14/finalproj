"""empty message

Revision ID: 89c27d795d51
Revises: a2a21eed04cf
Create Date: 2022-09-18 06:20:42.334797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89c27d795d51'
down_revision = 'a2a21eed04cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('apitoken', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'apitoken')
    # ### end Alembic commands ###