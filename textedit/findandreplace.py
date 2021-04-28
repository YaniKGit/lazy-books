import os
import re

texttofind = '. THE'
texttoreplace = ' The'

sourcepath = os.listdir('books/')

for file in sourcepath:
    inputfile = 'books/'+ file
    print('Conversion is ongoing for: ' + inputfile)
    with open(inputfile, 'r') as f:
        filedata = f.read()
        freq = 0
        freq = filedata.count(texttofind)
    destinationpath = 'rpbooks/' + file
    filedata = filedata.replace(texttofind, texttoreplace)
    # filedata = (re.sub('[a-z]*s*THE', 'the', filedata))
    with open(destinationpath, 'w') as file:
        file.write(filedata)
    print('Total %d Record Replaced' %freq + filedata)

for file in sourcepath:
    inputfile = 'books/'+ file
    print('Conversion is ongoing for: ' + inputfile)
    with open(inputfile, 'r') as f:
        filedata = f.read()
        freq = 0
        freq = filedata.count(texttofind)
    destinationpath = 'rpbooks/' + file
    # filedata = filedata.replace(texttofind, texttoreplace)
    filedata = (re.sub('[a-z]*s*THE', 'the', filedata))
    with open(destinationpath, 'w') as file:
        file.write(filedata)
    print('Total %d Record Replaced' %freq + filedata)