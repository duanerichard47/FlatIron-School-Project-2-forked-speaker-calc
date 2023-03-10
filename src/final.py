from pick import pick
from create_db import session
from sound_system import *

def designed_system():

    amp_power = ''

    if session.query(Amplifier).all() != []:
        amp_power = str(session.query(Amplifier).all()[0])

    if session.query(Speaker).all() != []:
        speakers = str(session.query(Speaker).all()[0])
        if int((str(session.query(Speaker.coils).all()[0]).split(",")[0]).split("(")[1]) > 1:
            xover = str(session.query(CrossOver).all()[0])
        else:
            xover = "No CrossOver, Single Coil Speaker"

    heading = 'Speaker System Designer\n\n' + amp_power + "\n\n" + speakers + "\n" + xover

    pick(['Done'], heading, "->")



# Typical system setup
# Analog Source or DAC -> Pre-amplifier -> Cross-Over or Equalizer -> Power Amplifier -> Speaker or set of speakers
