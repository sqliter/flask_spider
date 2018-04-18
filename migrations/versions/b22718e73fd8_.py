"""empty message

Revision ID: b22718e73fd8
Revises: 
Create Date: 2018-04-16 08:03:57.635293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b22718e73fd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('article_id', sa.String(length=20), nullable=False),
    sa.Column('article_title1', sa.String(length=100), nullable=False),
    sa.Column('article_text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('article_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('user_name', sa.String(length=30), nullable=True),
    sa.Column('nickname', sa.String(length=40), nullable=True),
    sa.Column('sex', sa.String(length=4), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('nickname'),
    sa.UniqueConstraint('user_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('article')
    # ### end Alembic commands ###
