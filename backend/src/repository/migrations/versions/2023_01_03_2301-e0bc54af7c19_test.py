"""test

Revision ID: e0bc54af7c19
Revises: a3e0c9c1ceef
Create Date: 2023-01-03 23:01:34.567372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0bc54af7c19'
down_revision = 'a3e0c9c1ceef'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.create_table(
    "account",
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("name", sa.String(length=64), nullable=False),
    sa.Column("email", sa.String(length=64), nullable=False),
    sa.Column("_hashed_password", sa.String(length=1024), nullable=True),
    sa.Column("_hash_salt", sa.String(length=1024), nullable=True),
    sa.Column("is_verified", sa.Boolean(), nullable=False),
    sa.Column("is_active", sa.Boolean(), nullable=False),
    sa.Column("is_logged_in", sa.Boolean(), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("email"),
    sa.UniqueConstraint("username"),
)
    


def downgrade() -> None:
    op.drop_table("account")
