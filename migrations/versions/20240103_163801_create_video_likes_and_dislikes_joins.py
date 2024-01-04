"""create_video_likes_and_dislikes_joins

Revision ID: ca969ee1b446
Revises: ca964cd120d4
Create Date: 2024-01-03 16:38:01.685217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ca969ee1b446"
down_revision = "ca964cd120d4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "videos_dislikes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("channelId", sa.Integer(), nullable=False),
        sa.Column("videoId", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["channelId"],
            ["channels.id"],
        ),
        sa.ForeignKeyConstraint(
            ["videoId"],
            ["videos.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "videos_likes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("channelId", sa.Integer(), nullable=False),
        sa.Column("videoId", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["channelId"],
            ["channels.id"],
        ),
        sa.ForeignKeyConstraint(
            ["videoId"],
            ["videos.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("videos_likes")
    op.drop_table("videos_dislikes")
    # ### end Alembic commands ###