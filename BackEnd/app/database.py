# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# URL de conexión a la base de datos PostgreSQL
# Puedes reemplazarla con la URL real de tu base de datos
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/eduleads")

# Creación del motor de la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,           # Tamaño del pool de conexiones
    max_overflow=0          # Número máximo de conexiones que puede crear cuando el pool está lleno
)

# Creación de una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para modelos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()