# """Databse helpers."""
# import sys
#
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import *
#
# db = SQLAlchemy()
#
#
# def get_db():
#     """Get all tables from database as Table objects."""
#     db.engine.connect()
#     metadata = MetaData()
#     metadata.reflect(db.engine)
#     return metadata
#
#
# def get_table(table_name):
#     """Get a Table object"""
#     metadata = get_db()
#     table = metadata.tables[table_name]
#     return table
#
#
# def get_table_contents(table_name, order):
#     """Select all from Table object, order by order"""
#     table = get_table(table_name)
#     query = select([table]).\
#         order_by(table.c[order])
#     return db.engine.execute(query).fetchall()
#
#
# def lookup_by_key(table_name, key_col, key):
#     """Select from table_name where table_name.key_col == key"""
#     table = get_table(table_name)
#     query = select([table]).\
#         where(table.c[key_col] == key)
#     return db.engine.execute(query).fetchone()
#
#
# def clean_data(data, columns):
#     """Remove items in `data` that don't correspond to a column in `columns`."""
#     return {x: y for (x, y) in data.items() if x in columns}
