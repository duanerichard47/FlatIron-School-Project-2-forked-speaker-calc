from sqlalchemy import (Index, Column, Integer, Float, String)
from create_db import Base

class Speaker(Base):
    __tablename__ = 'speakers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    power = Column(Integer())
    coils = Column(Integer())
    sensitivity = Column(Integer())
    ohms = Column(Float())
    min_freq = Column(Integer())
    max_freq = Column(Integer())

    def __repr__(self):
        return (f"{self.name}\n"
                f"Power: {self.power} Watts\n"
                f"Impedance: {self.ohms} Ohms\n"
                f"Frequency response: {self.min_freq} Hz - {self.max_freq} Hz")

class Amplifier(Base):
    __tablename__ = 'amplifier'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    power = Column(Integer())
    ohms = Column(Float())

    def __repr__(self):
        return f"{self.name}\nOutput: {self.power} watts"

class CrossOver(Base):
    __tablename__ = 'crossovers'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    cap_rating = Column(Float())
    ind_rating = Column(Float())

    def __repr__(self):
        return f"Tweeter Capacitor: {self.cap_rating} uF\nWoofer Inductor: {self.ind_rating} mH"
