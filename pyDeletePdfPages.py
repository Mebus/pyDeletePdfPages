#!/usr/bin/python3

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import os.path

input_file = sys.argv[1]

if os.path.isfile(input_file):

    infile = PdfFileReader(input_file, 'rb')
    output = PdfFileWriter()

     # zu löschende Seiten
    print('number of pages: ' + str(infile.getNumPages()))

    pages_to_delete = sys.argv[2].split(",")

    print("Deleting pages: " + str(pages_to_delete))

    for i in range(infile.getNumPages()):

        if not str(i+1) in pages_to_delete:
            p = infile.getPage(i)
            output.addPage(p)

    output_file =  'deleted_' + os.path.basename(input_file)

    with open(output_file, 'wb') as f:
        output.write(f)

    print("Output file: "+output_file)