"""add express boolean to package

Revision ID: fdbecaf262b5
Revises: f1b9ee79cb54
Create Date: 2020-06-25 16:55:28.634629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdbecaf262b5'
down_revision = 'f1b9ee79cb54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('packages', sa.Column('express', sa.Boolean(), server_default='False', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('packages', 'express')
    # ### end Alembic commands ###