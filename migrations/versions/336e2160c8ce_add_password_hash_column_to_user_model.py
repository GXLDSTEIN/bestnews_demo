"""Add password_hash column to User model

Revision ID: 336e2160c8ce
Revises: 8a5db1a1d558
Create Date: 2024-01-17 15:28:23.608033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '336e2160c8ce'
down_revision = '8a5db1a1d558'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
