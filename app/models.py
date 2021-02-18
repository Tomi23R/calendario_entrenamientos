from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Deporte(Enum):
    piscina = 1,
    aguas_abiertas = 2,
    carrera = 3,
    carrera_cinta = 4,
    bicicleta = 5,
    bicicleta_statica = 6,
    multideporte = 7
    gimnasio = 8

class TipoFecha(Enum):
    carga = 1,
    descarga =2,
    tappering = 3

class Repeticiones(Model):
    __tablename__ = 'repeticiones'
    id = Column(Integer, primary_key=True)
    # Numero de repeticiones
    num_rep = Column(Integer, default=1)
    # Distancia de cada repeticion (metros)
    distance = Column(Float)
    # Tiempo de cada repeticion (segundos)
    time = Column(Float)
    # Tiempo cada repetucion(Para series de natacion) en segundos
    each = Column(Integer)
    # Tiempo de descanso entre repeticiones (segundos)
    rest = Column(Integer)
    # Relacion many-to-one con bloques
    bloques_id = Column(Integer, ForeignKey('bloques.id'))
    # Relacion one-to-many con serie
    series = relationship('serie')

    # Para representar el modelo
    def __repr__(self):
        return '%d x %d' % (self.num_rep, self.distance)

class Serie(Model):
    __tablename__ = 'serie'
    id = Column(Integer, primary_key=True)
    # Ritmo de la serie (En metros/segundo)
    pace = Column(Float)
    # Distancia recorrida en la serie (metros)
    distance = Column(Float)
    # Frecuencia cardiaca
    hearthrate = Column(Integer)
    # Relacion many-to-one con repeticiones
    repeticiones_id = Column(Integer, ForeignKey('repeticiones.id'))
    
class Bloques(Model):
    __tablename__ = 'bloques'
    id = Column(Integer, primary_key=True)
    # Tiempo de descanso entre bloques (segundos)
    rest = Column(Integer)
    # Numero de bloques
    num_bloq = Column(Integer)
    # Relacion one-to-many con repeticiones
    repeticiones = relationship('Repeticiones')
    # Relacion many-to-one con entrenamiento
    entrenamiento_id = Column(Integer, ForeignKey('entrenamiento.id'))

class Entrenamiento(Model):
    __tablename__ = 'entrenamiento'
    id = Column(Integer, primary_key=True)
    # Nombre del entrenamiento
    name = Column(String(50), nullable=False)
    # Fecha del entrenamiento
    date = Column(DateTime, nullable=False)
    # Ritmo medio del entrenamiento (En metros/segundo)
    average_pace = Column(Float)
    # Tiempo total del entrenamiento (En segundos)
    time = Column(Float)
    # Distancia total del entrenamiento(metros)
    distance = Column(Float)
    # Percepcion de esfuerzo 1-10
    effort = Column(Integer)
    # Comentario del entreanamiento
    commentary = Column(String(100))
    # Tipo de deporte
    sport = Column(Enum(Deporte))
    # Relacion one-to-many con bloques
    bloques = relationship('Bloques')
    # Relacion many-to-one con usuario
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    # Relacion many-to-one con fechaCalendario
    fecha_calendario_id = Column(Integer, ForeignKey('fecha_calendario.id'))

    def __repr__(self):
        return self.name

class FechaCalendario(Model):
    __tablename__ = 'fecha_calendario'
    id = Column(Integer, primary_key=True)
    # Fecha del calendario
    date = Column(DateTime, nullable=False)
    # Comentarios en la fecha del calendario
    commentary = Column(String(100))
    # Que tipo de fecha es (carga, descarga, tappering)
    date_type = Column(Enum(TipoFecha))
    # Relacion one-to-many con entrenamientos
    entrenamientos = relationship('Entrenamiento')
    # Relacion many-to-one con calendario
    calendario_id = Column(Integer, ForeignKey('calendario.id'))

class Calendario(Model):
    __tablename__ = 'calendario'
    id = Column(Integer, primary_key=True)
    # Relacion one-to-many con fecha_calendario
    fechas = relationship('FechaCalendario')
    # Relacion one-to-one con usuario
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship('Usuario', back_populates='calendario')

class Usuario(Model):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    # Nombre del usuario
    name = Column(String(50), nullable=False)
    # Relacion one-to-one con calendario
    calendario = relationship('Calendario', uselist=False, back_populates='usuario')
    # Relacion one-to-many con entrenamientos
    records = relationship('Entrenamiento')

    def __repr__(self):
        return self.name