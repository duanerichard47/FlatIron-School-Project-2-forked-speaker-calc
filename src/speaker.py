from create_db import session
from sound_system import Speaker

def build_speakers():
    pass


# Need to define the following:
# id = Column(Integer(), primary_key=True)
# name = Column(String()) CAN BE ANY NAME
# power = Column(Integer()) USUALLY 50 watts TO 200 watts
# sensetivity = Column(Integer()) USUALLY 85 dB for most speakers (efficiency of converting current into sound)
# ohms = Column(Float()) USUALLY 8 Ohms sometimes 4 Ohms or 2 Ohms
# channel = Column(String()) Left or Right channel
# bass_port_len = Column(Float()) Length of bass port
# min_freq = Column(Integer()) Usually 20 Hz
# max_freq = Column(Integer()) Usually 20,000 Hz
