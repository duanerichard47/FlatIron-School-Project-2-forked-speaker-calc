from create_db import session
from sound_system import Speaker

import click
from pick import pick
import math

def build_speakers():

    title = ('Speaker Builder \n \n')

    description = ('This calculator creates a speaker box for use with your sound \n'
                   'system using the given specifications. \n')
    
    heading = title + description + ('\n Select Speaker Style')

    options = ['Component Speaker', 'Single Speaker']
    style, i_style = pick(options, heading, "->")

    print('\n ' + title)

    coils = 1

    if i_style == 0:
        coils = click.prompt(' Quantity of component speakers in speaker', default=2, type=click.IntRange(1))

    power = click.prompt(' Total watts output/input of speaker', default=80, type=click.IntRange(1))
    headroom = click.prompt(' Amplifier headroom in dB', default=3, type=click.IntRange(0))
    sensitivity = click.prompt(' Speaker sensitivity rating in dB', default=85, type=click.IntRange(1))

    click.clear()

    options = ['Yes', 'No']
    description = ('Power required: ' + str(power_required) + ' watts per channel\n\n'
                   'Assuming the speaker and amplifier output have the same \n'
                   'impedance of 8 ohms, the amplifier will need to have ' + str(power_required) + ' watts \n'
                   'of power to drive the speaker at ' + str(desired_level) + 'dB of SPL at ' + str(distance_from_source) + ' ' + units.lower() + 
                   '.\nThe speaker must also be able to handle this much power.\n')
    heading = title + description + ('\n Store this result?')

    store, index = pick(options, heading, "->")

    if index == 0:
        amp_name = 'Power Amplifier'

        if session.query(Amplifier).all() == []:
            session.add(Amplifier(name=amp_name, power=power_required, ohms=8))
        else:
            session.query(Amplifier).update({Amplifier.name: amp_name, Amplifier.power: power_required})

        session.commit()

    return power_required


# Need to define the following:
# id = Column(Integer(), primary_key=True)
# name = Column(String()) CAN BE ANY NAME
# power = Column(Integer()) USUALLY 50 watts TO 200 watts
# sensitivity = Column(Integer()) USUALLY 85 dB for most speakers (efficiency of converting current into sound)
# ohms = Column(Float()) USUALLY 8 Ohms sometimes 4 Ohms or 2 Ohms
# channel = Column(String()) Left or Right channel
# bass_port_len = Column(Float()) Length of bass port
# min_freq = Column(Integer()) Usually 20 Hz
# max_freq = Column(Integer()) Usually 20,000 Hz
