#!/usr/bin/env python

import click
from pick import pick

click.clear()
@click.command()

def nothing():
    pass

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
    
    print("")
    print(" " + title)
    print("")
    print(option)
    print(index)


