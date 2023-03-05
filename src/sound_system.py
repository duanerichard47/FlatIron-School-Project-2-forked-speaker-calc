from sqlalchemy import (Index, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
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
