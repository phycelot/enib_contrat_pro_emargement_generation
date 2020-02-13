from lib.pdf.transform_data import transform_data


def main():
    print("main")
    # data, week_number = get_data()
    data = {'Lundi':
                {'date': '02/03/20', 'lessons': [
                    {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'],
                     'students': ['09PO-IAS'],
                     'rooms': ['2-E205'], 'start_hour': {'h': 8, 'm': 5}, 'duration': {'h': 1, 'm': 30}},
                    {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'],
                     'students': ['09PO-IAS'],
                     'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}},
                    {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'],
                     'students': ['09PO-IAS'],
                     'rooms': ['B005'], 'start_hour': {'h': 12, 'm': 45}, 'duration': {'h': 1, 'm': 30}},
                    {'module': 'IAS', 'course': 'IA et Jeu Vidéo', 'teachers': ['BOSSER Anne-Gwenn'],
                     'students': ['09PO-IAS'],
                     'rooms': ['B005'], 'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}}]},
            'Mardi':
                {'date': '03/03/20', 'lessons': [
                    {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'],
                     'students': ['07PO-MSI'], 'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40},
                     'duration': {'h': 1, 'm': 30}},
                    {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'],
                     'students': ['07PO-MSI'], 'rooms': ['2-E205'], 'start_hour': {'h': 11, 'm': 15},
                     'duration': {'h': 1, 'm': 30}},
                    {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'],
                     'students': ['07PO-MSI'], 'rooms': ['2-E205', 'B015'], 'start_hour': {'h': 14, 'm': 20},
                     'duration': {'h': 1, 'm': 30}},
                    {'module': 'MSI', 'course': 'Méta-modélisation', 'teachers': ['CHEVAILLIER Pierre'],
                 'students': ['07PO-MSI'], 'rooms': ['2-E205', 'B015'], 'start_hour': {'h': 15, 'm': 55},
                 'duration': {'h': 1, 'm': 30}}]}, 'Mercredi': {'date': '04/03/20', 'lessons': [
            {'module': 'PRI', 'course': 'Sprint 0 : Backlog',
             'teachers': ['DESMEULLES Gireg', 'GLEMAREC Yann', 'KUBICKI Sebastien', 'LEGELEUX Amélie'],
             'students': ['09PO-PRI'], 'rooms': [''], 'start_hour': {'h': 8, 'm': 5}, 'duration': {'h': 1, 'm': 30}},
            {'module': 'PRI', 'course': 'Sprint 0 : Backlog', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''],
             'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}},
            {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''],
             'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}},
            {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''],
             'start_hour': {'h': 15, 'm': 55}, 'duration': {'h': 1, 'm': 30}},
            {'module': 'PRI', 'course': 'Sprint 0', 'teachers': [''], 'students': ['09PO-PRI'], 'rooms': [''],
             'start_hour': {'h': 17, 'm': 30}, 'duration': {'h': 1, 'm': 30}}]},
            'Jeudi': {'date': '05/03/20',
                      'lessons': [{'module': 'ERI',
                                   'course': 'low tech',
                                   'teachers': [
                                       'TOQUET Delphine'],
                                   'students': [
                                       '09PX-ERI'],
                                   'rooms': [
                                       'Stiff'],
                                   'start_hour': {
                                       'h': 8,
                                                                                                            'm': 5},
                                                                                                        'duration': {
                                                                                                            'h': 1,
                                                                                                            'm': 30}},
                                  {'module': 'ERI',
                                                                                                        'course': 'low tech',
                                                                                                        'teachers': [
                                                                                                            'TOQUET Delphine'],
                                                                                                        'students': [
                                                                                                            '09PX-ERI'],
                                                                                                        'rooms': [
                                                                                                            'Stiff'],
                                                                                                        'start_hour': {
                                                                                                            'h': 9,
                                                                                                            'm': 40},
                                                                                                        'duration': {
                                                                                                            'h': 1,
                                                                                                            'm': 30}}]},
            'Vendredi': {'date': '06/03/20', 'lessons': [
                {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'],
                 'rooms': ['2-E205'], 'start_hour': {'h': 9, 'm': 40}, 'duration': {'h': 1, 'm': 30}},
                {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'],
                 'rooms': ['2-E205'], 'start_hour': {'h': 11, 'm': 15}, 'duration': {'h': 1, 'm': 30}},
                {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'],
                 'rooms': ['B013'], 'start_hour': {'h': 14, 'm': 20}, 'duration': {'h': 1, 'm': 30}},
                {'module': 'REV', 'course': 'OpenGL', 'teachers': ['NEDELEC Alexis'], 'students': ['09PO-REV'],
                 'rooms': ['B013'], 'start_hour': {'h': 15, 'm': 55}, 'duration': {'h': 1, 'm': 30}}]}}
    week_number = 10
    print(data)
    data_dict = transform_data(data, week_number)
    print(data_dict)
    # generate_pdf(data)

if __name__ == '__main__':
    main()
