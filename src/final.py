from pick import pick
from create_db import session
from sound_system import *

def designed_system():

    amp_power = ''

    if session.query(Amplifier).all() != []:
        amp_power = str(session.query(Amplifier).all()[0])

    heading = 'Speaker System Designer\n\n' + amp_power

    pick(['Done'], heading, "->")


# Typical system setup
# Analog Source or DAC -> Pre-amplifier -> Power Amplifier -> Speaker or set of speakers
