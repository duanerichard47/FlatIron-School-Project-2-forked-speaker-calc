#!/usr/bin/env python

import click
from pick import pick
from sqlalchemy import create_engine
from create_db import Base, engine
from final import designed_system
from amp_power import amplifier_power_required

click.clear()
@click.command()

def main_menu():
    run_menu = True

    title = 'Speaker System Designer'
    
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
               'View Designed System',
               'Exit Application']
    
    while run_menu == True:
        option, index = pick(options, title, "->")
    
        if index == 0:
            amplifier_power_required()
        elif index == 1:
            pass
        elif index == 2:
            pass
        elif index == 3:
            pass
        elif index == 4:
            pass
        elif index == 5:
            pass
        elif index == 6:
            pass
        elif index == 7:
            pass
        elif index == 8:
            pass
        elif index == 9:
            pass
        elif index == 10:
            pass
        elif index == 11:
            pass
        elif index == 12:
            pass
        elif index == 13:
            pass
        elif index == 14:
            pass
        elif index == 15:
            pass
        elif index == 16:
            pass
        elif index == 17:
            pass
        elif index == 18:
            designed_system()
        else:
            print("\n All done.\n\n")
            run_menu = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main_menu()
