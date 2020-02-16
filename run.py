from configparser import ConfigParser
from datetime import datetime

from data.constants import TEMPLATE_PATH, CONFIG_PATH
from lib.edt.edt import get_data
from lib.pdf.generate import write_fillable_pdf
from lib.pdf.transform_data import transform_data


def main():
    data, week_number = get_data()
    data_dict = transform_data(data, week_number)

    config = ConfigParser()
    config.read(CONFIG_PATH)

    last_name = str(config.get('user', 'student_fullname')).split(" ")[0]
    output_filename = "TrameEmargementContratPro_{}_Semaine_{}_{}.pdf".format(last_name,week_number,datetime.now().year)
    write_fillable_pdf(input_pdf_path=TEMPLATE_PATH,output_pdf_path=output_filename,data_dict=data_dict)


if __name__ == '__main__':
    main()
