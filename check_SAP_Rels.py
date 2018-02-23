import os.path, datetime;

t = ['05', '5555', '5000', '0555']

def checkFile(file):
    if os.path.isfile(file) == True:
        if datetime.date.fromtimestamp(os.path.getmtime(file)).day == (datetime.date.today().day - 1):
            return file.lstrip('//p01/out/') + ': NICE'
    else:
        return file.lstrip('//p01/out/') + ': DAMN, SON!'

for i in tipos:
    filepath1 = "//p01/out/zzz_"+ i +".txt"
    filepath2 = "//p01/out/zzy_"+ i +".txt"
    filepath3 = "//p01/out/zzx_"+ i +".txt"
    filepath4 = "//p01/out/zxy_"+ i +".txt"

    print(checkFile(filepath1), checkFile(filepath2), checkFile(filepath3), checkFile(filepath4))
