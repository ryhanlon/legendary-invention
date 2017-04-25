"""
This file is written by Rebecca Hanlon.

"""


def greeting(name, age):
    """
    Calls questions() then outputs the greeting and adjusted age.
    :param name: string
    :param age: integer
    :return: None
    """
    age_next_year = age + 1
    print(f"""
        Hello {name}!  Greetings from ZeeBot Alpha Centauri!  
        We wish you a happy birthday next year when you will be {age_next_year} years old.
        """)

def questions():
    """
    Gets name and age.
    :return: None
    """
    name = input(f"What is your name? >> ")
    age = int(input(f"How old are you? >> "))

    greeting(name, age)


questions()

