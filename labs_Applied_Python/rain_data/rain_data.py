"""
This file was written by Rebecca Hanlon.  Gathers the data to find the highest total rainfall per month.

"""

import os


RAIN_DIR = '/Users/MacBookPro/Git/Projects_FSP/labs_Applied_Python/rain_data/'


def file_handler(filesystem_path: str) -> str:
    with open(filesystem_path, 'r') as f:
        raw_text = f.read()
        return raw_text


raw_data = file_handler(os.path.join(RAIN_DIR, 'sample.rain'))


def summary(by_date: dict) -> None:

    most_rain_day = max(by_date.items(), key=lambda t: t[1][0])
    date, average_rainfall = most_rain_day[0], int(most_rain_day[1][0]/24)

    year, yearly_average = most_rain_day[0][7:11], most_rain_day[1][0]

    print(f"On {date} the average rain fall was: {average_rainfall} inches.")

    print(year, yearly_average)






def clean_data():

    split_data = raw_data.split('\n')
    no_header = split_data[11:]
    single_lines = [line.split() for line in no_header]
    clean_lines = [line for line in single_lines if line != []]

    by_date = {data[0]: (int(data[1]), list(map(int, data[2:]))) for data in clean_lines if '-' not in data[2:]}

    summary(by_date)


clean_data()


#os.listdir(RAIN_DIR)