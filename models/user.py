from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.session import engine, meta_data

users = Table("users", meta_data,
              Column("id", Integer, primary_key=True, index=True),
              Column("name", String(255), nullable=False),
              Column("username", String(255), nullable=False),
              Column("email", String(255), nullable=False, unique=True, index=True),
              Column("password", String(255), nullable=False, unique=True),
              Column("is_active", Boolean, default=True),
              Column("is_superuser", Boolean, default=False)
              )

meta_data.create_all(engine)
