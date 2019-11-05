#!/usr/bin/env python3
import eml_parser
import glob
import base64
import pdftotext
import io, re
import datetime
from operator import itemgetter

filenames = glob.glob("eml/*.eml")

# parse through each of the eml files, we are only expecting one attachment which is the pdf of results

def eml_to_pdf(filename):
    with open(filename, 'rb') as fhdl:
        raw_email = fhdl.read()
        parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email, include_attachment_data=True)
        raw_attachment_data = parsed_eml['attachment'][0]['raw']
        return base64.b64decode(raw_attachment_data)

pdfs = [eml_to_pdf(filename) for filename in filenames]

inr_regex = "Your INR result was:\W+(\d\.\d) on (\d\d?/\d\d?/\d\d\d\d)"
data = []
for pdf in pdfs:
    pdf_text = pdftotext.PDF(io.BytesIO(pdf))
    m = re.search(inr_regex, pdf_text[0])
    day, month, year = m.group(2).split("/")
    data.append([float(m.group(1)), datetime.date(int(year), int(month), int(day))])

data = sorted(data, key=itemgetter(1))
print("Date,INR")
for d in data:
    print(d[1].isoformat() + "," + str(d[0]))
