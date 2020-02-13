import json
from configparser import ConfigParser

from data.constants import DAYS_NAME, CONFIG_PATH


def transform_data(parsed_edt, week_number):
    data_dict = dict()
    with open('config/pdf_config.json') as json_file:
        data = json.load(json_file)
        # header
        print(data)
        header = data.get('header')
        # load config
        config = ConfigParser()
        config.read(CONFIG_PATH)
        student_fullname = config.get('user', 'student_fullname')
        company = config.get('user', 'company')
        training_date = config.get('user', 'training_date')
        data_dict[header.get('student_fullname')] = student_fullname
        data_dict[header.get('company')] = company
        data_dict[header.get('student_fullname')] = student_fullname
        data_dict[header.get('training_date')] = training_date
        data_dict[header.get('week_number')] = str(week_number)

        # week
        week = data.get('week')

        days_name = DAYS_NAME
        for day_name in days_name:
            day = week.get(day_name)
            print(day)
            conf = parsed_edt.get(day_name)
            print(conf)
            data_dict[day.get('date')] = str(conf.get("date"))

            lessons = conf.get('lessons')
    return data_dict
