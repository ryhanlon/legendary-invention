"""
This is a file written by Rebecca Hanlon.
This module converts the width, height and cost of paint to give the use the number 
of gallons and cost of paint.
"""
import math


def area_calculation(width, height, cost, coats):
    """
    Ask for the width, height, cost and coats to be painted.
    :param width: int
    :param height: int
    :param cost: int
    :param coats: int
    :return: None
    """
    area = width * height

    result = area / 400

    number_gallons = math.ceil(result * coats)
    gallons_cost = number_gallons * cost

    print(f"You will need {number_gallons} gallons of paint.  It will cost ${gallons_cost}.")



def wall_info():
    """
    Ask for:  width of the wall | height of the wall | how much gallon of paint costs
    
    """
    width_info = float(input("Enter the width of the wall. >> "))
    height_info = float(input("Enter the height of the wall. >> "))
    cost_info = float(input("How much does each gallon of paint cost? >> "))
    coats_info = float(input("How many coats will you do? >> "))


    walls  = input("Do you have another wall to paint?  Y/yes or N/no ")
    if walls == "y".lower():
        wall_info()
    else:
        area_calculation(width_info, height_info, cost_info, coats_info)



wall_info()

