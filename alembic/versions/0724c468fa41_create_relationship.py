"""create relationship

Revision ID: 0724c468fa41
Revises: c3bf998f7529
Create Date: 2023-03-25 09:27:43.318526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0724c468fa41'
down_revision = 'c3bf998f7529'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'message_logs',
        sa.Column('member_id', sa.Integer, sa.ForeignKey("members.user_id")),
    )


def downgrade() -> None:
    op.drop_column('message_logs','member_id')
