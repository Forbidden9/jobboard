from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from config.config import settings

# Conexion a la base de datos
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# if you don't want to install postgres or any database, use sqlite, a file system based database,
# uncomment below lines if you would like to use sqlite and comment above 2 lines of SQLALCHEMY_DATABASE_URL AND engine

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

meta_data = MetaData()

# Transaccion para la serie de transacciones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
