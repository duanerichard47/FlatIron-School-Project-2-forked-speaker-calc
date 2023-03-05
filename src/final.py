from pick import pick
from create_db import session
from sound_system import *

def designed_system():
    heading = (
        'Speaker System Designer\n\n'
        ' Power Amplifier Output: 10 watts'
        )

    pick(['Done'], heading, "->")
