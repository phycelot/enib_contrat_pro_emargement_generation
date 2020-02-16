from configparser import ConfigParser
from datetime import datetime

from data.constants import TEMPLATE_PATH, CONFIG_PATH
from lib.edt.edt import get_data
from lib.pdf.generate import write_fillable_pdf
from lib.pdf.transform_data import transform_data


def main():
    data, week_number = get_data()
    # data = {'Lundi':
    #             {'date': '02/03/20', 'lessons': [
    #                 {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'],
    #                  'students': ['09PO-IAS'],
    #                  'rooms': ['2-E205'], 'start_hour': {'h': 8, 'm': 5}, 'duration': {'h': 1, 'm': 30}},
    #                 {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'],
    #                  'students': ['09PO-IAS'],
    #                  'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}},
    #                 {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'],
    #                  'students': ['09PO-IAS'],
    #                  'rooms': ['B005'], 'start_hour': {'h': 12, 'm': 45}, 'duration': {'h': 1, 'm': 30}},
    #                 {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'],
    #                  'students': ['09PO-IAS'],
    #                  'rooms': ['B005'], 'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}}]},
    #         'Mardi':
    #             {'date': '03/03/20', 'lessons': [
    #                 {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'],
    #                  'students': ['07PO-MSI'], 'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40},
    #                  'duration': {'h': 1, 'm': 30}},
    #                 {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'],
    #                  'students': ['07PO-MSI'], 'rooms': ['2-E205'], 'start_hour': {'h': 11, 'm': 15},
    #                  'duration': {'h': 1, 'm': 30}},
    #                 {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'],
    #                  'students': ['07PO-MSI'], 'rooms': ['2-E205', 'B015'], 'start_hour': {'h': 14, 'm': 20},
    #                  'duration': {'h': 1, 'm': 30}},
    #                 {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'],
    #                  'students': ['07PO-MSI'], 'rooms': ['2-E205', 'B015'], 'start_hour': {'h': 15, 'm': 55},
    #                  'duration': {'h': 1, 'm': 30}}]}, 'Mercredi': {'date': '04/03/20', 'lessons': [
    #         {'module': 'PRI', 'course': 'Sprint 0 : Backlog',
    #          'teachers': ['DESMEULLES Gireg', 'GLEMAREC Yann', 'KUBICKI Sebastien', 'LEGELEUX Amélie'],
    #          'students': ['09PO-PRI'], 'rooms': [''], 'start_hour': {'h': 8, 'm': 5}, 'duration': {'h': 1, 'm': 30}},
    #         {'module': 'PRI', 'course': 'Sprint 0 : Backlog', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''],
    #          'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}},
    #         {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''],
    #          'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}},
    #         {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''],
    #          'start_hour': {'h': 15, 'm': 55}, 'duration': {'h': 1, 'm': 30}},
    #         {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''],
    #          'start_hour': {'h': 17, 'm': 30}, 'duration': {'h': 1, 'm': 30}}]},
    #         'Jeudi': {'date': '05/03/20',
    #                   'lessons': [{'module': 'ERI',
    #                                'course': 'low tech',
    #                                'teachers': [
    #                                    'TOQUET Delphine'],
    #                                'students': [
    #                                    '09PX-ERI'],
    #                                'rooms': [
    #                                    'Stiff'],
    #                                'start_hour': {
    #                                    'h': 8,
    #                                    'm': 5},
    #                                'duration': {
    #                                    'h': 1,
    #                                    'm': 30}},
    #                               {'module': 'ERI',
    #                                'course': 'low tech',
    #                                'teachers': [
    #                                    'TOQUET Delphine'],
    #                                'students': [
    #                                    '09PX-ERI'],
    #                                'rooms': [
    #                                    'Stiff'],
    #                                'start_hour': {
    #                                    'h': 9,
    #                                    'm': 40},
    #                                'duration': {
    #                                    'h': 1,
    #                                    'm': 30}}]},
    #         'Vendredi': {'date': '06/03/20', 'lessons': [
    #             {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'],
    #              'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}},
    #             {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'],
    #              'rooms': ['2-E205'], 'start_hour': {'h': 11, 'm': 15}, 'duration': {'h': 1, 'm': 30}},
    #             {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'],
    #              'rooms': ['B013'], 'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}},
    #             {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'],
    #              'rooms': ['B013'], 'start_hour': {'h': 15, 'm': 55}, 'duration': {'h': 1, 'm': 30}}]}}
    # week_number = 10
    # print(data)
    data_dict = transform_data(data, week_number)
    config = ConfigParser()
    config.read(CONFIG_PATH)
    last_name = str(config.get('user', 'student_fullname')).split(" ")[0]
    output_filename = "TrameEmargementContratPro_{}_Semaine_{}_{}.pdf".format(last_name,week_number,datetime.now().year)
    write_fillable_pdf(input_pdf_path=TEMPLATE_PATH,output_pdf_path=output_filename,data_dict=data_dict)


if __name__ == '__main__':
    main()
