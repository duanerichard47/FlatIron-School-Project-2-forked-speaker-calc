#!/usr/bin/env python

import click
from pick import pick
import math

click.clear()
@click.command()


def amplifier_power_required():
    distance_from_source = click.prompt('Listener distance from source in meters', default=100)
    desired_level = click.prompt('Desired dB SPL at distance', default=85)
    sensitivity = click.prompt('Sensitivity rating in dB', default=88)
    headroom = click.prompt('Amplifier headroom in dB', default=3)
    reference_distance = 1

    power_required = int(10 ** (((desired_level + headroom - sensitivity) + 20 * math.log((distance_from_source / reference_distance), 10)) / 10))

    print("Power required: " + str(power_required) + " watts")
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

