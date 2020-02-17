import os
import pdfkit
import sys

files = []

for file in os.listdir():
    if file.endswith(".html"):
        files.append(file)
files.sort()

folder = os.path.basename(os.getcwd())

if len(sys.argv) == 2 and sys.argv[1] == '-l':
    option = {'orientation': 'Landscape'} 
    filename = folder + "L.pdf"
    pdfkit.from_file(files, filename, options=option)
else:
    filename = folder + ".pdf"
    pdfkit.from_file(files, filename)