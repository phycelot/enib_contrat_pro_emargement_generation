import getpass
from configparser import ConfigParser

from twisted.python.compat import raw_input

from data.constants import CONFIG_PATH
from . import parse_edt
from .edt_connexion import EdtConnexion


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
