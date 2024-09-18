from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Bancos(Base):
    __tablename__ = "bancos"
    id_bancos = Column(Integer, primary_key=True, index=True)
    ba_nom = Column(String(50), nullable=False)
    ba_act = Column(String(1), nullable=False)
    id_pais = Column(Integer, ForeignKey("pais.id_pais"))

    pais = relationship("Pais", back_populates="bancos")


class Pais(Base):
    __tablename__ = "pais"
    id_pais = Column(Integer, primary_key=True, index=True)
    p_nomb = Column(String(40), nullable=False)
    p_mone = Column(String(3), nullable=False)
    p_act = Column(String(1), nullable=False)

    bancos = relationship("Bancos", back_populates="pais")


class Emisor(Base):
    __tablename__ = "emisor"
    id_emisor = Column(Integer, primary_key=True, index=True)
    e_docu = Column(String(15), nullable=False)
    e_nomb = Column(String(50), nullable=False)
    e_apel = Column(String(50), nullable=False)
    e_telf = Column(String(9), nullable=False)
    e_mail = Column(String(50))


class Receptor(Base):
    __tablename__ = "receptor"
    id_receptor = Column(Integer, primary_key=True, index=True)
    r_docu = Column(String(15), nullable=False)
    r_nomb = Column(String(50), nullable=False)
    r_apel = Column(String(50), nullable=False)
    r_telf = Column(String(10))
    r_email = Column(String(50))
    r_tipcuen = Column(String(1), nullable=False)
    r_numcuen = Column(String(30), nullable=False)
    id_bancos = Column(Integer, ForeignKey("bancos.id_bancos"))

    bancos = relationship("Bancos")


class Tasas(Base):
    __tablename__ = "tasas"
    id_tasa = Column(Integer, primary_key=True, index=True)
    ta_descri = Column(String(35), nullable=False)
    ta_mond = Column(String(3), nullable=False)
    ta_cambio = Column(Numeric(15, 7), nullable=False)
    ta_act = Column(String(1), nullable=False)
    ta_fecha = Column(DateTime, nullable=False, default=datetime.utcnow)


class Transaccion(Base):
    __tablename__ = "transaccion"
    id_transac = Column(Integer, primary_key=True, index=True)
    t_fecha = Column(DateTime, nullable=False, default=datetime.utcnow)
    t_monte = Column(Numeric(12, 5), nullable=False)
    t_montr = Column(Numeric(12, 5), nullable=False)
    t_descrip = Column(String(30), nullable=False)
    t_estado = Column(String(1), nullable=False)
    id_user = Column(Integer, ForeignKey("usuarios.id_user"))
    id_tasa = Column(Integer, ForeignKey("tasas.id_tasa"))
    id_emisor = Column(Integer, ForeignKey("emisor.id_emisor"))
    id_receptor = Column(Integer, ForeignKey("receptor.id_receptor"))
    id_pais = Column(Integer, ForeignKey("pais.id_pais"))


class Usuarios(Base):
    __tablename__ = "usuarios"
    id_user = Column(Integer, primary_key=True, autoincrement=True, index=True)
    u_nombr = Column(String(50), nullable=False)
    u_email = Column(String(50), nullable=False)
    u_pass = Column(String(20), nullable=False)
    u_act = Column(String(1), nullable=False)
    u_tipo = Column(String(1), nullable=False)
    u_fechcrea = Column(DateTime, nullable=False, default=datetime.utcnow)
    u_fechlogi = Column(DateTime, nullable=False, default=datetime.utcnow)


DATABASE_URL = "postgresql://postgres:1234@localhost:5432/remesas"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
