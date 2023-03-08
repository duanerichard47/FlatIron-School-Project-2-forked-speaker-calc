from create_db import session
from sound_system import Speaker, CrossOver

import click
from pick import pick
import math

def build_speakers():

    title = ('Speaker Builder \n \n')

    description = ('This calculator creates a speaker box for use with your sound \n'
                   'system using the given specifications. \n')
    
    heading = title + description + ('\n Select Speaker Style')

    options = ['2-Way Cross-Over Speaker', 'Single Speaker']
    style, i_style = pick(options, heading, "->")

    print('\n ' + title)

    coil_count = 1
    capacitor = 0
    inductor = 0
    fx_range = [20, 20000]

    if i_style == 0:
        help = (' Crossovers are used to filter certain frequencies from a driver.\n'
              ' A High Pass Filter (HPF) filters out low frequencies - for example,\n'
              ' removing bass from a tweeter. A Low Pass Filter (LPF) filters out\n'
              ' high frequencies - for example, removing treble from a woofer.\n'
              ' Crossovers are necessary to prevent overlap in frequency response\n'
              ' from different drivers in a system, and to prevent a driver from\n'
              ' producing frequencies it was not designed for.\n')
        
        heading = title + help + ('\n Select Filtering Style of Cross-Over')

        coil_count = 2

        options = ['1st Order Butterworth', '1st Order Solen Split (-6 dB)']
        style, c_style = pick(options, heading, "->")

        if c_style == 0:
            c_ratio = 0.1590
            l_ratio = 0.1592
        else:
            c_ratio = 0.1125
            l_ratio = 0.2251

        hfi = click.prompt(' Driver Impedance of the High Frequency Driver in Ohms', default=8, type=click.IntRange(1))
        lfi = click.prompt(' Driver Impedance of the Low Frequency Driver in Ohms', default=8, type=click.IntRange(1))
        cfx = click.prompt(' Crossover Frequency in Hz', default=400, type=click.IntRange(1))

        capacitor = (c_ratio / (hfi * cfx)) * 1000000 # in uF on + side of tweeter
        inductor = ((l_ratio * lfi) / cfx) * 1000 # in mH on + side of woofer

        total_ohms = (1 / ((1/hfi) + (1/lfi))) # Simplified calculation
    else:
        total_ohms = click.prompt(' Total resistance of speaker in Ohms', default=8, type=click.IntRange(1))

    power_draw = click.prompt(' Total watts output/input of speaker', default=30, type=click.IntRange(1))
    total_sensitivity = click.prompt(' Speaker sensitivity rating in dB', default=85, type=click.IntRange(1))

    click.clear()

    options = ['Yes', 'No']
    if coil_count > 1:
        description = ('New speaker specifications\n\n'
                    'Speaker power: ' + str(power_draw) + ' watts \n'
                    'Speaker sensitivity: ' + str(total_sensitivity) + ' dB \n'
                    'Speaker impedance: ' + str(total_ohms) + ' Ohms \n'
                    'Tweeter capacitor: ' + str(capacitor) + ' uF \n'
                    'Woofer inductor: ' + str(inductor) + ' mH \n'
                    'Cross-Over Frequency: ' + str(cfx) + ' Hz \n'
                    'Frequency response: 20 Hz - 20,000 Hz \n')
    else:
        description = ('New speaker specifications\n\n'
                    'Speaker power: ' + str(power_draw) + ' watts \n'
                    'Speaker sensitivity: ' + str(total_sensitivity) + ' dB \n'
                    'Speaker impedance: ' + str(total_ohms) + ' Ohms \n'
                    'Frequency response: 20 Hz - 20,000 Hz \n')
        
    heading = title + description + ('\n Store this result?')

    store, index = pick(options, heading, "->")

    if index == 0:
        spk_name = 'Speaker'
        x_name = 'CrossOver'

        if session.query(Speaker).all() == []:
            session.add(Speaker(name=spk_name, 
                                power=power_draw, 
                                coils=coil_count, 
                                sensitivity=total_sensitivity, 
                                ohms=total_ohms,
                                min_freq=fx_range[0],
                                max_freq=fx_range[1]))
            session.add(CrossOver(name=x_name, 
                                cap_rating=capacitor,
                                ind_rating=inductor))
        else:
            session.query(Speaker).update({Speaker.name: spk_name,
                                           Speaker.power: power_draw,
                                           Speaker.coils: coil_count,
                                           Speaker.sensitivity: total_sensitivity,
                                           Speaker.ohms: total_ohms,
                                           Speaker.min_freq: fx_range[0],
                                           Speaker.max_freq: fx_range[1]})
            session.query(CrossOver).update({CrossOver.name: x_name,
                                           CrossOver.cap_rating: capacitor,
                                           CrossOver.ind_rating: inductor})
        session.commit()

    return None

