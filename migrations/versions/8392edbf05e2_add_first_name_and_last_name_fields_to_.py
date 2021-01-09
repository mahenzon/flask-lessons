"""add first_name and last_name fields to User

Revision ID: 8392edbf05e2
Revises: b9099d27ef2d
Create Date: 2021-01-09 16:23:03.697440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8392edbf05e2'
down_revision = 'b9099d27ef2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=120), server_default='', nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=120), server_default='', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###