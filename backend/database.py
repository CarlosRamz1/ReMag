from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import Base

# Connection string de Supabase (sin exponer contraseña)
DATABASE_URL = "postgresql://postgres:Carloz34$$5$#@db.gfgwidxspjfioghlogjj.supabase.co:5432/postgres"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ejecutar la migración para crear tablas
print("Iniciando migración...")
Base.metadata.create_all(bind=engine)
print("✅ Migración completada: Tablas creadas en Supabase")