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
    cap_rating = Column(Float())
    ind_rating = Column(Float())
    min_freq = Column(Integer())
    max_freq = Column(Integer())

    def __repr__(self):
        if self.coils > 1:
            xover = f"Tweeter Capacitor: {self.cap_rating} uF\nWoofer Inductor: {self.ind_rating} mH"
        else:
            xover = 'No Cross-Over, Single Speaker'

        return (f"{self.name}\n"
                f"Power: {self.power} Watts\n"
                f"{xover}\n"
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

class CrossOver:
    pass

class Equalizer:
    pass

class DigitalAnalogConverter:
    pass

class DigitalSoundProcessor:
    pass
