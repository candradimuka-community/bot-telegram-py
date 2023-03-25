"""create members table

Revision ID: c3bf998f7529
Revises: a2cb8030f295
Create Date: 2023-03-25 09:14:11.937072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3bf998f7529'
down_revision = 'a2cb8030f295'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'members',
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, unique=True),
        sa.Column('name', sa.String),
    )


def downgrade() -> None:
    op.drop_table('members')
