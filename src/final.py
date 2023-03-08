from pick import pick
from create_db import session
from sound_system import *

def designed_system():

    amp_power = ''

    if session.query(Amplifier).all() != []:
        amp_power = str(session.query(Amplifier).all()[0])

    if session.query(Speaker).all() != []:
        speakers = str(session.query(Speaker).all()[0])

    heading = 'Speaker System Designer\n\n' + amp_power + "\n\n" + speakers

    pick(['Done'], heading, "->")

