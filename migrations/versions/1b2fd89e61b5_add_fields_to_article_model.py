"""add fields to Article model

Revision ID: 1b2fd89e61b5
Revises: 6c1355a96172
Create Date: 2021-01-10 12:34:55.894425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b2fd89e61b5'
down_revision = '6c1355a96172'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('body', sa.Text(), server_default='', nullable=False))
    op.add_column('article', sa.Column('dt_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('article', sa.Column('dt_updated', sa.DateTime(), nullable=True))
    op.add_column('article', sa.Column('title', sa.String(length=200), server_default='', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'title')
    op.drop_column('article', 'dt_updated')
    op.drop_column('article', 'dt_created')
    op.drop_column('article', 'body')
    # ### end Alembic commands ###
