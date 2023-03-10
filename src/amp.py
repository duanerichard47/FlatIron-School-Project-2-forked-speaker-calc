from create_db import session
from sound_system import Amplifier

import click
from pick import pick
import math

def amplifier_power_required():

    title = ('Amplifier Power Required \n \n')

    description = ('This calculator provides the required electrical power \n'
                   '(power output from the amplifier) to produce a desired \n'
                    'Sound Pressure Level (SPL) at a given distance, along \n'
                    'with an amount of headroom to keep the amplifier(s) \n'
                    'out of clip. \n')
    
    heading = title + description + ('\n Select Units')

    options = ['Meters', 'Feet']
    units, index = pick(options, heading, "->")

    print('\n ' + title)

    if index == 0:
        distance_from_source = click.prompt(' Listener distance from speaker (in meters)', default=3.7, type=click.FloatRange(0.01))
        reference_distance = 1
    else:
        distance_from_source = click.prompt(' Listener distance from speaker (in feet)', default=12.0, type=click.FloatRange(0.01))
        reference_distance = 3.281

    desired_level = click.prompt(' Desired dB SPL at this distance', default=80, type=click.IntRange(1))
    headroom = click.prompt(' Amplifier headroom in dB', default=3, type=click.IntRange(0))
    sensitivity = click.prompt(' Speaker sensitivity rating in dB', default=85, type=click.IntRange(1))
    total_ohms = click.prompt(' Amplifier impedance in Ohms', default=8, type=click.IntRange(1))

    power_required = 10 ** (((desired_level + headroom - sensitivity) + 20 * math.log((distance_from_source / reference_distance), 10)) / 10)

    if power_required < 1:
        power_required = round(power_required, 4)
    else:
        power_required = int(power_required)

    click.clear()

    options = ['Yes', 'No']
    description = ('Power required: ' + str(power_required) + ' watts per channel\n\n'
                   'Assuming the speaker and amplifier output have the same \n'
                   'impedance of ' + str(total_ohms) + ' ohms, the amplifier will need to have ' + str(power_required) + ' watts \n'
                   'of power to drive the speaker at ' + str(desired_level) + 'dB of SPL at ' + str(distance_from_source) + ' ' + units.lower() + 
                   '.\nThe speaker must also be able to handle this much power.\n')
    heading = title + description + ('\n Store this result?')

    store, index = pick(options, heading, "->")

    if index == 0:
        amp_name = 'Power Amplifier'

        if session.query(Amplifier).all() == []:
            session.add(Amplifier(name=amp_name, power=power_required, ohms=total_ohms))
        else:
            session.query(Amplifier).update({Amplifier.name: amp_name,
                                             Amplifier.power: power_required,
                                             Amplifier.ohms: total_ohms})

        session.commit()

    return power_required
