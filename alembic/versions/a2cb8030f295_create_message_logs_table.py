"""create message logs table

Revision ID: a2cb8030f295
Revises: 
Create Date: 2023-03-25 09:05:08.775555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2cb8030f295'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'message_logs',
        sa.Column('message_id', sa.Integer, primary_key=True),
        sa.Column('message_data', sa.JSON),
        sa.Column('created_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('message_logs')
