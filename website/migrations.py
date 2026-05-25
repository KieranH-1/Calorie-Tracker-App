from alembic import op
import sqlalchemy as sa
from models import User, Food, UserFood

# Table Operations
# op.create_table('table_name', sa.Column('id', sa.Integer, primary_key=True))
# op.drop_table('table_name')
# Column Operations
# op.add_column('table_name', sa.Column('new_column', sa.String(50)))
# op.drop_column('table_name', 'column_name')
# Index Operations
# op.create_index('index_name', 'table_name', ['column_name'])
# op.drop_index('index_name', 'table_name')
# Constraint Operations
# op.create_foreign_key('fk_name', 'source_table', 'referent_table', ['local_cols'], ['remote_cols'])
# op.drop_constraint('fk_name', 'source_table', type_='foreignkey')
# Data Operations
# op.execute("UPDATE table_name SET column_name = 'new_value' WHERE condition")
# op.bulk_insert('table_name', [{'column1': 'value1', 'column2': 'value2'}, {'column1': 'value3', 'column2': 'value4'}])
