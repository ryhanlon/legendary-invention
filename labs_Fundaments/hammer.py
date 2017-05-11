"""
Write a function that returns the meal for any given hour of the day.

Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM

>>> meal(7)
'Breakfast time.'
>>> meal(13)
'Lunch time.'
>>> meal(20)
'Dinner time.'
>>> meal(21)
'No meal scheduled at this time.'
>>> meal(0)
'No meal scheduled at this time.'
>>> meal(3)
'Hammer time.'
>>> meal(9999)
'Not a valid time.'


"""

# returns the meal for any hour

def meal(time):
    if time > 24:
        result = 'Not a valid time.'

    elif time >= 7 and time < 9:
        result = 'Breakfast time.'

    elif time >= 12 and time < 14:
        result = 'Lunch time.'

    elif time >= 19 and time < 21:
        result = 'Dinner time.'

    elif (time >= 22 and time <24) or (time < 4 and time >=0):
        result = 'Hammer time.'

    elif ()
        result = 'No meal scheduled at this time.'


    return result






