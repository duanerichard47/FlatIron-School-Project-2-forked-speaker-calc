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
    
    options = ['Amplifier Power Calculator',
               'Speaker Builder',
               'View Designed System',
               'Exit Application']
    
    while run_menu == True:
        option, index = pick(options, title, "->")
    
        if index == 0:
            amplifier_power_required()
        elif index == 1:
            pass
        elif index == 2:
            designed_system()
        else:
            print("\n All done.\n\n")
            run_menu = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main_menu()
