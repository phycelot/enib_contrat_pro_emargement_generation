from twisted.python.compat import raw_input
import getpass

from edt_connexion import EdtConnexion
import parse_edt
from configparser import ConfigParser

import os
import pdfrw



CONFIG_PATH = 'config/config.ini'
INVOICE_TEMPLATE_PATH = 'data/TrameEmargementAlternant·e2019_Diffusion.pdf'
INVOICE_OUTPUT_PATH = 'trame.pdf'

def main():
    print("main")
    # data = get_data()
    data = {'Lundi': {'date': '02/03/20', 'lessons': [{'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'], 'students': ['09PO-IAS'], 'rooms': ['2-E205'], 'start_hour': {'h': 8, 'm': 5}, 'duration': {'h': 1, 'm': 30}}, {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'], 'students': ['09PO-IAS'], 'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}}, {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'], 'students': ['09PO-IAS'], 'rooms': ['B005'], 'start_hour': {'h': 12, 'm': 45}, 'duration': {'h': 1, 'm': 30}}, {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'], 'students': ['09PO-IAS'], 'rooms': ['B005'], 'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}}]}, 'Mardi': {'date': '03/03/20', 'lessons': [{'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'], 'students': ['07PO-MSI'], 'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}}, {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'], 'students': ['07PO-MSI'], 'rooms': ['2-E205'], 'start_hour': {'h': 11, 'm': 15}, 'duration': {'h': 1, 'm': 30}}, {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'], 'students': ['07PO-MSI'], 'rooms': ['2-E205', 'B015'], 'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}}, {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'], 'students': ['07PO-MSI'], 'rooms': ['2-E205', 'B015'], 'start_hour': {'h': 15, 'm': 55}, 'duration': {'h': 1, 'm': 30}}]}, 'Mercredi': {'date': '04/03/20', 'lessons': [{'module': 'PRI', 'course': 'Sprint 0 : Backlog', 'teachers': ['DESMEULLES Gireg', 'GLEMAREC Yann', 'KUBICKI Sebastien', 'LEGELEUX Amélie'], 'students': ['09PO-PRI'], 'rooms': [''], 'start_hour': {'h': 8, 'm': 5}, 'duration': {'h': 1, 'm': 30}}, {'module': 'PRI', 'course': 'Sprint 0 : Backlog', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}}, {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''], 'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}}, {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''], 'start_hour': {'h': 15, 'm': 55}, 'duration': {'h': 1, 'm': 30}}, {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''], 'start_hour': {'h': 17, 'm': 30}, 'duration': {'h': 1, 'm': 30}}]}, 'Jeudi': {'date': '05/03/20', 'lessons': [{'module': 'ERI', 'course': 'low tech', 'teachers': ['TOQUET Delphine'], 'students': ['09PX-ERI'], 'rooms': ['Stiff'], 'start_hour': {'h': 8, 'm': 5}, 'duration': {'h': 1, 'm': 30}}, {'module': 'ERI', 'course': 'low tech', 'teachers': ['TOQUET Delphine'], 'students': ['09PX-ERI'], 'rooms': ['Stiff'], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}}]}, 'Vendredi': {'date': '06/03/20', 'lessons': [{'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'], 'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}}, {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'], 'rooms': ['2-E205'], 'start_hour': {'h': 11, 'm': 15}, 'duration': {'h': 1, 'm': 30}}, {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'], 'rooms': ['B013'], 'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}}, {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'], 'rooms': ['B013'], 'start_hour': {'h': 15, 'm': 55}, 'duration': {'h': 1, 'm': 30}}]}}
    generate_pdf(data)

def generate_pdf(data):
    print(data)
    # get template
    template_pdf = pdfrw.PdfReader(INVOICE_TEMPLATE_PATH)

    # process

    # save pdf
    pdfrw.PdfWriter().write(INVOICE_OUTPUT_PATH, template_pdf)

def get_data():
    print("initiating")

    try:
        # load config
        config = ConfigParser()
        config.read(CONFIG_PATH)

        # login
        login = config.get('user', 'login')
        if not login:
            login = raw_input('Login: ')
        else:
            print('Login: {}'.format(login))

        # password
        password = getpass.getpass('Password: ')

        print("we have all needed data")

        # connexion and build data
        edt_connexion = EdtConnexion(login=login, password=password, edt_url="https://edt.enib.fr/timetable_groups.php")
        print("login...")
        if not edt_connexion.do_login():
            print('login failed')
            get_data()
            return
        edt_connexion.rebuild_form_cache()
        print('login success')
        config.set('user', 'login', login)

        # student data
        student_id = config.get('user', 'student_id')
        student_fullname = config.get('user', 'student_fullname')
        if student_id and student_fullname:
            print("Student Fullname: {}".format(student_fullname))
            print("Student ID: {}".format(student_id))
        else:
            student_id = None
            while not student_id:
                student_fullname = raw_input('Student Fullname (ex: DUPOND Jean) : ')
                student_id = edt_connexion.get_students().get(student_fullname)
                if student_id is None:
                    print("student not found")
            config.set('user', 'student_id', student_id)
            config.set('user', 'student_fullname', student_fullname)

        # get edt data for this week
        week_number = int(raw_input('Week Number : '))
        edt = edt_connexion.get_student_edt(student_id, week_number)
        parsed_edt = parse_edt.get_parsed_edt(edt)

        # get company detail
        company = config.get('user', 'company')
        while not company:
            company = raw_input('Company Name and City (ex: ENIB - Brest) : ')
        config.set('user', 'company', company)

        training_date = config.get('user', 'training_date')
        while not training_date:
            training_date = raw_input('Training Date (ex: DU 05/09/2019 AU 04/09/2020) : ')
        config.set('user', 'training_date', training_date)

        # save config
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)

        return parsed_edt
    except KeyboardInterrupt:
        return None
    except Exception as error:
        print('ERROR', error)
        return get_data()


if __name__ == '__main__':
    main()
