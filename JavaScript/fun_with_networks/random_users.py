"""
This file is written by Rebecca Hanlon.

"""

import requests





def display_users(users):

    for user in users:
        name_data = user.get('name')
        first_name = name_data['first']
        last_name = name_data['last']
        email = user.get('email')
        user_name = user.get('login')['username']
        reg_name = user.get('registered')
        date_of_birth = user.get('dob')
        print(f"""Name: {first_name} {last_name}
Email: {email}
Username: {user_name}
Registration Date: {reg_name}
Birth Date: {date_of_birth}
    """)


def get_users(info: str) -> dict:
    response = requests.get(info)
    users = response.json().get("results")
    display_users(users)


get_users(info="http://api.randomuser.me/?results=5")

