import db
from sqlalchemy import Column, Integer,Integer,Float,Float
class Producto(db.Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True)
    VALOR = Column(Integer, nullable=False)
    MEDIA = Column(Float)
    DESVIACION = Column(Float)
    DESVIACION_AL_CUADRADO = Column(Float)
  
    def __init__(self, VALOR, MEDIA, DESVIACION, DESVIACION_AL_CUADRADO):
        self.VALOR = VALOR
        self.MEDIA = MEDIA
        self.DESVIACION = DESVIACION
        self.DESVIACION_AL_CUADRADO = DESVIACION_AL_CUADRADO
    def __repr__(self):
        return f'Producto({self.VALOR}, {self.MEDIA}, {self.DESVIACION}, {self.DESVIACION_AL_CUADRADO})'
