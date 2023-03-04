#!/usr/bin/env python

import click
from pick import pick
import math

click.clear()
@click.command()


def amplifier_power_required():
    print('Amplifier Power Required')
    print('')
    print('This calculator provides the required electrical power '
          '(power output from the amplifier) to produce a desired Sound Pressure Level (SPL) '
          'at a given distance, along with an amount of headroom to keep the amplifier(s) out of clip.')
    print('')

    units = click.prompt('Use meters or feet? Default is', default="meters")

    if units == "meters":
        distance_from_source = click.prompt('Listener distance from speaker (in meters)', default=3.7)
        reference_distance = 1
    elif units == "feet":
        distance_from_source = click.prompt('Listener distance from speaker (in feet)', default=12.0)
        reference_distance = 3.281
    else:
        print('Incorrect units specified.')
        return 0

    if distance_from_source <= 0:
        print('Distance must be greater than 0.')
        return 0

    desired_level = click.prompt('Desired dB SPL at distance', default=80)
    sensitivity = click.prompt('Speaker sensitivity rating in dB', default=85)
    headroom = click.prompt('Amplifier headroom in dB', default=3)

    power_required = 10 ** (((desired_level + headroom - sensitivity) + 20 * math.log((distance_from_source / reference_distance), 10)) / 10)

    if power_required < 1:
        power_required = round(power_required, 4)
    else:
        power_required = int(power_required)

    print('')
    print('Power required: ' + str(power_required) + ' watts')
    print('')
    print('What does this mean?')
    print('Assuming the speaker and amplifier output have the same impedance, '
          'the amplifier will need to have ' + str(power_required) + ' watts of power to drive the speaker speaker at '
          + str(desired_level) + 'dB of SPL at ' + str(distance_from_source) + ' ' + str(units) + '. The speaker must also be able to handle this much power.')

    return power_required

if __name__ == '__main__':

    title = 'Speaker System Design Calculator'
    
    options = ['Amplifier Power Required',
               'Ohm\'s Law / Watt\'s Law',
               'db Voltage Ratio',
               'db Power Ratio',
               'Inverse Square Law',
               'Transformer Delivered Power',
               'Speaker Box Enclosure Designer',
               'Speaker Box Volume Designer',
               'Sealed or Ported Enclosure',
               'Driver Displacement',
               '2-Way Crossover',
               '3-Way APC Crossover',
               'Series Notch Filter',
               'Parallel Notch Filter',
               'Driver Attenuation Circuit',
               'Impedance Equalizer',
               'Contour Network',
               'Air Core Inductor Designer',
               'Exit Application']
    
    option, index = pick(options, title, "->")
    
    if index == 0:
        amplifier_power_required()
    elif index == 1:
        print(option)
    elif index == 2:
        print(option)
    elif index == 3:
        print(option)
    elif index == 4:
        print(option)
    elif index == 5:
        print(option)
    elif index == 6:
        print(option)
    elif index == 7:
        print(option)
    elif index == 8:
        print(option)
    elif index == 9:
        print(option)
    elif index == 10:
        print(option)
    elif index == 11:
        print(option)
    elif index == 12:
        print(option)
    elif index == 13:
        print(option)
    elif index == 14:
        print(option)
    elif index == 15:
        print(option)
    elif index == 16:
        print(option)
    elif index == 17:
        print(option)
    else:
        print("Bye!")

