from sqlalchemy import (Index, Column, Integer, Float, String)
from create_db import Base

class Enclosure:
    pass

class Speaker(Base):
    __tablename__ = 'speakers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    power = Column(Integer())
    ohms = Column(Float())
    channel = Column(String())
    port_length = Column(Float())
    min_freq = Column(Integer())
    max_freq = Column(Integer())

class Amplifier(Base):
    __tablename__ = 'amplifier'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    power = Column(Integer())
    ohms = Column(Float())

    def __repr__(self):
        return f"{self.name} Output = {self.power} watts"

class Preamplifier:
    pass

class Receiver:
    pass

class CrossOver:
    pass

class Equalizer:
    pass

class DigitalAnalogConverter:
    pass

class DigitalSoundProcessor:
    pass
