#!/usr/bin/env python3
import eml_parser
import glob
import base64

filenames = glob.glob("eml/*.eml")

# parse through each of the eml files, we are only expecting one attachment which is the pdf of results
def eml_to_pdf(filename):
    with open(filename, 'rb') as fhdl:
        raw_email = fhdl.read()
        parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email, include_attachment_data=True)
        raw_attachment_data = parsed_eml['attachment'][0]['raw']
        return base64.b64decode(raw_attachment_data)

pdf = [eml_to_pdf(filename) for filename in filenames]
with open('test.pdf', 'wb') as p_out:
    p_out.write(pdf[0])
