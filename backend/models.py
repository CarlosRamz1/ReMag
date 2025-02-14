from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido_paterno = Column(String, nullable=False)
    apellido_materno = Column(String, nullable=False)
    nss = Column(String, unique=True, nullable=False)
    unidad_medica = Column(String, nullable=False)

class Cita(Base):
    __tablename__ = 'citas'
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    fecha = Column(Date, nullable=False)
    tipo_servicio = Column(String, nullable=False)

class Servicio(Base):
    __tablename__ = 'servicios'
    id = Column(Integer, primary_key=True, index=True)
    cita_id = Column(Integer, ForeignKey('citas.id'))
    estudio = Column(String, nullable=False)

class Reporte(Base):
    __tablename__ = 'reportes'
    id = Column(Integer, primary_key=True, index=True)
    servicio_id = Column(Integer, ForeignKey('servicios.id'))
    detalles = Column(String, nullable=False)
