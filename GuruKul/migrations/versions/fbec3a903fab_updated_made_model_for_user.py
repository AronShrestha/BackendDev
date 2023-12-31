"""updated  made model for user

Revision ID: fbec3a903fab
Revises: 5589f0b16c85
Create Date: 2023-08-03 20:04:44.849858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbec3a903fab'
down_revision = '5589f0b16c85'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
