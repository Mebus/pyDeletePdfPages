#!/usr/bin/python3

from PyPDF2 import PdfWriter, PdfReader
import sys
import os.path

input_file = sys.argv[1]

if os.path.isfile(input_file):

    infile = PdfReader(input_file, 'rb')
    output = PdfWriter()

     # zu löschende Seiten
    print(f'number of pages: {len(infile.pages)}')

    pages_to_delete = sys.argv[2].split(",")

    print(f"Deleting pages: {str(pages_to_delete)}")

    for i in range(len(infile.pages)):
        if not str(i+1) in pages_to_delete:
            p = infile.pages[i]
            output.add_page(p)

    output_file =  'deleted_' + os.path.basename(input_file)

    with open(output_file, 'wb') as f:
        output.write(f)

    print("Output file: "+output_file)