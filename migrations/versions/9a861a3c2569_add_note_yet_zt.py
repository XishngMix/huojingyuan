"""add note_yet zt

Revision ID: 9a861a3c2569
Revises: 
Create Date: 2019-01-07 12:13:40.324528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a861a3c2569'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note_yet', sa.Column('zt', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note_yet', 'zt')
    # ### end Alembic commands ###
