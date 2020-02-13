# -*-coding:utf8-*-

from bs4 import BeautifulSoup

import re
import datetime

debug_rdts = (datetime.time(9, 30),  # H1
              datetime.time(11, 5),  # H2
              datetime.time(12, 40),  # H3
              datetime.time(14, 10),  # H4
              datetime.time(15, 45),  # H5
              datetime.time(17, 20),  # H6
              datetime.time(18, 55))  # H7


def getStrHn(hour):
    for i, h in enumerate(debug_rdts):
        if hour == h:
            return f"H{i + 1}"

        elif hour < h:
            return "H{}+ ({})".format(i, hour.strftime("%H:%M"))


def extract_all(div):
    data = dict()

    line = div.find_all("p", recursive=False)
    titre = div.find_all("h1", recursive=False)[0].text

    data['module']=titre.split(" ")[1].split("-")[1]

    d = line[1:]
    if "Enseignant" in d[1].text and "Etudiant" in d[2].text and "Salle" in d[3].text:
        data['course'] = d[0].text
        data['teachers'] = str_list_to_list(d[1].text.split(":")[1])
        data['students'] = str_list_to_list(d[2].text.split(":")[1])
        data['rooms'] = str_list_to_list(d[3].text.split(":")[1])

    dates = re.findall(r'(2[0-3]|[01]?[0-9]):([0-5]?[0-9])', line[0].text)
    data['start_hour'] = tuple_hour_to_dict(dates[0])
    data['duration'] = tuple_hour_to_dict(dates[1])

    return data


def tuple_hour_to_dict(in_tuple):
    data = dict()
    data['h'] = int(in_tuple[0])
    data['m'] = int(in_tuple[1])
    return data


def str_list_to_list(str_list):
    str_list = str_list.split(',')
    return [n.strip() for n in str_list]


def get_parsed_edt(data):
    """
    data from edt to json
    :param data:
    :return:
    """
    soup = BeautifulSoup(data, "html.parser")
    edt_table = soup.find("table", {"class": "thinborder"})

    if not edt_table:
        return False

    parsed_edt = {}

    days = edt_table.find_all("tr", recursive=False)[2:]

    for day in days:
        test = day.find_all("div", {"class", "help"})

        blocks = day.find_all("td", recursive=False)



        str_day = blocks[0].find_all("b")[0].text.strip()

        date = blocks[0].text.strip(str_day)

        lessons = [extract_all(t) for t in test]

        data = {
            "date" : date,
            "lessons": lessons
        }

        parsed_edt[str_day] = data
    return parsed_edt
