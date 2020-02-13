import pdfrw

from data.constants import INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, ANNOT_KEY, SUBTYPE_KEY, WIDGET_SUBTYPE_KEY, \
    ANNOT_FIELD_KEY


def generate_pdf(data_dict):
    print(data_dict)
    # get template
    template_pdf = pdfrw.PdfReader(INVOICE_TEMPLATE_PATH)

    # process
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )

    # save pdf
    pdfrw.PdfWriter().write(INVOICE_OUTPUT_PATH, template_pdf)
