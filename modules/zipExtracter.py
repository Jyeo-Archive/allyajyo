import sys
import zipfile
from threading import Thread
def extractzip(zFile, password):
    try:
        zFile.extractall(pwd=password)
        sys.stdout.write("!!PASSWORD FOUND!! password is '%s'\n"%password)
    except:
        pass
def ZipExtracter(filename, dicname):
    try:
        zFile=zipfile.Zipfile(filename)
        try:
            f=open(dicname, 'r')
            for password in f.readlines():
                t=Thread(target=extractzip, args=(zFile, password))
                t.start()
            f.close()
        except IOError:
            sys.stdout.write("dictionary file not found\n")
    except IOError:
        sys.stdout.write("zip file not found\n")
