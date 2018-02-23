#CAUAN_KMS, Feb 23rd 2018
#Checking if DB.mdb is ready

import os.path

if os.path.isfile("//ap669/DB.mdb") == True:
    print('NICE')
else:
    print('DAMN, SON!')
