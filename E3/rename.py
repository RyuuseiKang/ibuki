from base64 import decode
import os
from os import walk

import sys
print(sys.getdefaultencoding())

import unicodedata


f = []
for (dirpath, dirnames, filenames) in walk(os.path.dirname(os.path.abspath(__file__))):
    f.extend(filenames)
    
    for file in filenames:
        
        str = unicodedata.normalize('NFC', file)

        str = str.encode('CP949')
        str = str.decode('shift-jis')

        os.rename(file, str)
        print(file + ' -> ' + str)
    break