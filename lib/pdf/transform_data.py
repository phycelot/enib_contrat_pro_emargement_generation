import json


def transform_data(parsed_edt):
    with open('config/pdf_config.json') as json_file:
        data = json.load(json_file)
        print(data)
        print(data.get('header'))
        print(data.get('week'))
    data_dict = parsed_edt
    return data_dict
