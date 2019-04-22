"""add Note_yet reason

Revision ID: 30a52f222336
Revises: 3465f5f5fbfd
Create Date: 2019-01-10 22:06:52.152671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30a52f222336'
down_revision = '3465f5f5fbfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note_yet', sa.Column('reason', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note_yet', 'reason')
    # ### end Alembic commands ###
