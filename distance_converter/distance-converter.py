"""
This file is written by Rebecca Y. Hanlon.

"""

def converter():

    input_distance = int(input("Enter distance:  "))
    input_unit = input("Enter units (meter, kilometer, feet, mile):  ")
    target_units = input("Enter target units (meter, kilometer, feet, mile):  ")

    # convert
    if input_unit == 'meter' or input_unit == 'm':
        distance = input_distance * 1

    elif input_unit == 'kilometer' or input_unit == 'km':
        unit = input_unit * .001

        #distance = input_distance * .001

    elif input_unit == 'mile' or input_unit == 'mi':
        unit = input_unit * .0006

        #distance = input_distance * .0006



    1 meter = 3 feet
    1 meter = .001 kilometer
    1 meter = .0006 mile