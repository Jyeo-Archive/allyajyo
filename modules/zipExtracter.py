import sys
import zipfile
from threading import Thread
def passwordGenerator(num): #num=>생성할 비밀번호 자리수
    pw_list=[]
    count=0
    for i in range(0, 10**num):
        pw_list.append(str(count).zfill(num))
        count+=1
    return pw_list
class zip:
    def __init__(self, filename, mode): #self 인스턴스, zip filename, extract mode
        self.zFile=zipfile.ZipFile(filename)
        self.passwordfound=False
    def extractzip(self, password):
        if self.passwordfound is True:
            pass
        else:
            try:
                zFile.extractall(pwd=bytes(password, 'UTF-8'))
                sys.stdout.write("!!PASSWORD FOUND!! password is '%s'\n"%password)
                self.passwordfound=True
            except:
                sys.stdout.write("Trying password '%s'...\n"%password)
    def ZipDictionary(self):
        try:
            zFile=zipfile.ZipFile(filename)
            try:
                f=open(dicname, 'r')
                for password in f.readlines():
                    password=password.strip('\n')
                    t=Thread(target=extractzip, args=(zFile, password))
                    t.start()
                f.close()
            except IOError:
                sys.stdout.write('dictionary file not found\n')
        except IOError:
            sys.stdout.write('zip file not found\n')
    def ZipBrute(self):
        zFile=zipfile.ZipFile(filename)
        min_range=input("input password min digits : ")
        max_range=input("input password max digits : ")
        for i in range(min_range, max_range):
            pw_list=passwordGenerator(i)
            for password in pw_list:
                t=Thread(target=extractzip, args=(zFile, password))
                t.start()
        if self.passwordfound is False:
            sys.stdout.write('password not found in range ')
            for i in range(0, min_range):
                sys.stdout.write('0')
            sys.stdout.write(' ~ ')
            for i in range(0, max_range):
                sys.stdout.write('9')
    def setmode(self, mode): #모드설정
        if mode==1:
            ZipDictionary() #사전대입
        else:
            ZipBrute() #브루트포싱
