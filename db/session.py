from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from config.config import settings

# Conexion a la base de datos
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

meta_data = MetaData()

# Transaccion para la serie de transacciones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Conexion con una session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
