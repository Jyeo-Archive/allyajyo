import sys
import zipfile
from time import sleep #delay를 위해 time의 sleep import
from threading import Thread
def passwordGenerator(num): #num=>생성할 비밀번호 자리수
    pw_list=[]
    count=0
    for i in range(0, 10**num):
        pw_list.append(str(count).zfill(num))
        count+=1
    return pw_list
class zip:
    def __init__(self, filename): #self 인스턴스, zip filename
        self.zFile=zipfile.ZipFile(filename)
        self.passwordfound=False
    def extractzip(self, password):
        if self.passwordfound is True:
            return
        else:
            try:
                self.zFile.extractall(pwd=bytes(password, 'UTF-8'))
                sys.stdout.write("!!PASSWORD FOUND!! password is '%s'\n"%password)
                self.passwordfound=True
            except:
                sys.stdout.write("Trying password '%s'...\n"%password)
    def ZipDictionary(self, dicname):
        try:
            f=open(str(dicname), 'r')
            for password in f.readlines():
                self.process=0;
                password=password.strip('\n')
                if self.passwordfound is False:
                    t=Thread(target=self.extractzip, args=(password,))
                    t.start()
                    self.process+=1
            f.close()
            if self.passwordfound is False:
                sys.stdout.write('password not found in dictionary')
        except IOError:
            sys.stdout.write('dictionary file not found\n')
    def ZipBrute(self):
        min_range=int(input("input password min digits : "))
        max_range=int(input("input password max digits : "))
        for i in range(min_range, max_range+1):
            pw_list=passwordGenerator(i)
            for password in pw_list:
                if self.passwordfound is False:
                    t=Thread(target=self.extractzip, args=(password,))
                    t.start()
                else:
                    pass
        if self.passwordfound is False:
            sys.stdout.write('password not found in range ')
            for i in range(0, min_range):
                sys.stdout.write('0')
            sys.stdout.write(' ~ ')
            for i in range(0, max_range):
                sys.stdout.write('9')
            sys.stdout.write('\n')
    def setmode(self, mode, dicname): #모드설정
        if mode==1:
            self.ZipDictionary(dicname) #사전대입
        elif mode==2:
            self.ZipBrute() #브루트포싱
        else:
            sys.stdout.write('not a vaild mode\n')
