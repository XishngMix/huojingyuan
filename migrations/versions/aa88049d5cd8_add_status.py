"""add status

Revision ID: aa88049d5cd8
Revises: 30a52f222336
Create Date: 2019-01-28 04:48:16.797109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa88049d5cd8'
down_revision = '30a52f222336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note_yet', sa.Column('status', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note_yet', 'status')
    # ### end Alembic commands ###
