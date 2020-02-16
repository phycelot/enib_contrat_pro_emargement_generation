import json
from configparser import ConfigParser

from data.constants import DAYS_NAME, CONFIG_PATH, HOURS_NAME, HOURS_DATA
from lib.utils.string import teachers_dict_to_teacher


def transform_data(edt_data, week_number):
    output_data = dict()
    with open('config/pdf_config.json') as json_file:
        config_data = json.load(json_file)
        # header
        # print(config_data)
        header = config_data.get('header')

        # load config
        config = ConfigParser()
        config.read(CONFIG_PATH)
        student_fullname = config.get('user', 'student_fullname')
        company = config.get('user', 'company')
        training_date = config.get('user', 'training_date')
        output_data[header.get('student_fullname')] = student_fullname
        output_data[header.get('company')] = company
        output_data[header.get('student_fullname')] = student_fullname
        output_data[header.get('training_date')] = training_date
        output_data[header.get('week_number')] = str(week_number)

        # config_data_week
        config_data_week = config_data.get('week')

        days_name = DAYS_NAME
        for day_name in days_name:
            config_data_day = config_data_week.get(day_name)
            edt_data_day = edt_data.get(day_name)
            output_data[config_data_day.get('date')] = str(edt_data_day.get("date"))

            edt_data_lessons = edt_data_day.get('lessons')
            config_data_lessons = config_data_day.get('lessons')

            i = 0
            for config_data_lesson in config_data_lessons:
                # print(config_data_lesson)
                # print(HOURS_NAME[i])
                # print(HOURS_DATA[HOURS_NAME[i]])
                for edt_data_lesson in edt_data_lessons:
                    if edt_data_lesson.get('start_hour') == HOURS_DATA[HOURS_NAME[i]].get('start_hour'):
                        # print('ok')
                        # print(edt_data_lesson)
                        output_data[config_data_lesson.get('teacher')] = teachers_dict_to_teacher(edt_data_lesson.get("teachers"))
                        output_data[config_data_lesson.get('module')] = str(edt_data_lesson.get("module"))
                        break
                i += 1
    return output_data
