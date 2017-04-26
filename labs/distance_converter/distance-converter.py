"""
This file is written by Rebecca Y. Hanlon.

"""

# catch input errors, refactor, add additional units

def converter():

    input_distance = int(input("Enter distance:  "))
    input_unit = input("Enter units (m, km, ft, mi):  ")
    target_unit = input("Enter target units (m, km, ft, mi):  ")
    m_to_meters = input_unit == 'meter' or input_unit == 'm'
    km_to meters = input_unit == 'kilometer' or input_unit == 'km'

    # convert units to meter
    if to_meters:
        distance = input_distance * 1       # m to m
        print(distance)

    elif km_to meters:
        distance = input_distance * 1000   # km to m
        print(distance)

    elif input_unit == 'mile' or input_unit == 'mi':
        distance = input_distance * 1609    # mi to m
        print(distance)

    elif input_unit == 'feet' or input_unit == 'ft':
        distance = input_distance * .3    # ft to m
        print(distance)

    # convert input units to target units
    if target_unit == 'meter' or target_unit == 'm':
        convert_dist = distance * 1       # m to m
        print(f"{input_distance} {input_unit} is {convert_dist} m")

    elif target_unit == 'kilometer' or target_unit == 'km':
        convert_dist = distance * .001  # m to km
        print(f"{input_distance} {input_unit} is {convert_dist} km")

    elif target_unit == 'mile' or target_unit == 'mi':
        convert_dist = distance * .0006    # m to mi
        print(f"{input_distance} {input_unit} is {convert_dist} mi")
    elif target_unit == 'feet' or target_unit == 'ft':
        convert_dist = distance * 3.3    # m to ft
        print(f"{input_distance} {input_unit} is {convert_dist} ft")


converter()