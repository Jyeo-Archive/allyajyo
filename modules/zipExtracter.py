import sys
import zipfile
from threading import Thread
def extractzip(zFile, password):
    try:
        zFile.extractall(pwd=password)
        sys.stdout.write('!!PASSWORD FOUND!! password is '%s'\n'%password)
    except:
        pass
def ZipDictionary(filename, dicname):
    try:
        zFile=zipfile.Zipfile(filename)
        try:
            f=open(dicname, 'r')
            for password in f.readlines():
                t=Thread(target=extractzip, args=(zFile, password))
                t.start()
            f.close()
        except IOError:
            sys.stdout.write('dictionary file not found\n')
    except IOError:
        sys.stdout.write('zip file not found\n')
def ZipBrute(filename):
    try:
        zFile=zipfile.Zipfile(filename)
        for password in range(0, 1000):
            t=Thread(target=extractzip, args=(zFile, str(password)))
            t.start()
        f.close()
    except IOError:
        sys.stdout.write('zip file not found\n')
def zipExtracter(mode, filename, dicname):
    if mode=='dic':
        ZipDictionary(filename, dicname)
    else:
        ZipBrute(filename)
