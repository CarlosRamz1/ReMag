from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connection string de Supabase (sin exponer contraseña)
DATABASE_URL = "postgresql://postgres:Carloz34$$5$#@db.gfgwidxspjfioghlogjj.supabase.co:5432/postgres"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

