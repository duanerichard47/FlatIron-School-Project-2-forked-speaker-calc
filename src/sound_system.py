from sqlalchemy import (Index, Column, Integer, String)
from create_db import Base

class Enclosure:
    pass

class Speaker:
    pass

class Tweeter:
    pass

class Midrange:
    pass

class Woofer:
    pass

class Amplifier(Base):
    __tablename__ = 'amplifier'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    power = Column(Integer())

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
