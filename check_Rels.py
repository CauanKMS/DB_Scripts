#CauanKMS, Feb 23rd 2018

import os.path, datetime
import win32api as win

repsSrc = "//sm1/dpout/"

def checkFile(file):
    modTimeFile = datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime("%d/%m/%Y %H:%M")

    if os.path.isfile(file) == True:
        return file.lstrip(repsSrc) + ': NICE, ' + modTimeFile
    else:
        return file.lstrip(repsSrc) + ': DAMN, SON! ' + modTimeFile

ti = ['0005', '5555', '0555', '0055']
fileReps = ["r04_", "o2_","019_G_", "pr7_"]

##########
# BD.mdb #
##########

filepath_ap70 = "//ap70/"
filepathBD = filepath_ap70 + "BD.mdb"

tryagain = True

while(tryagain == True):
    try:
        modTimeFileBD = datetime.datetime.fromtimestamp(os.path.getmtime(filepathBD)).strftime("%d/%m/%Y %H:%M")
        print('\n' + filepathBD.lstrip(filepath_ap70) + ': ONLINE, ' + modTimeFileBD)
        tryagain = False

    except:
        print('\n' + filepathBD.lstrip(filepath_ap70) + ': OFFLINE')
        tryagain = True

###########
# REPORTS #
###########

for f in fileReps:
    for t in tipos:
        filepath = repsSrc + f + t + ".txt"
        print(checkFile(filepath))

win.MessageBox(0, 'CHECK THE FILES!', 'DONE!')

