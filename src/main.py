#!/usr/bin/env python

import click
from pick import pick
from amp_power import amplifier_power_required

click.clear()
@click.command()

def main_menu():
    run_menu = True

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
    
    while run_menu == True:
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
            print("\n All done.\n\n")
            run_menu = False


if __name__ == '__main__':
    main_menu()
