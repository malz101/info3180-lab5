"""empty message

Revision ID: 10dae57ffcf2
Revises: 7619bb5dff3e
Create Date: 2021-03-06 09:46:17.863091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10dae57ffcf2'
down_revision = '7619bb5dff3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
