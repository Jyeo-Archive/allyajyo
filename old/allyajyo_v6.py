#allyajyo_v6.py

import os
import sys
import base64
import pefile
def getFileExtension(file_name):
	file_extenstion=os.path.splitext(file_name)[1]
	return file_extenstion
class database: #database class
	'''
	usage
		fruitDB=database() #init new database named fruitDB
		fruitDB.set("fruitDB.txt") #set database file to "fruitDB.txt"
		fruitDB.add("apple") #add item "apple" to fruitDB
		fruitDB.delate("apple") #delate item "apple" from fruitDB
	'''
	def __init__(self, DBfilename):
		self.filename=DBfilename
	def add(self, data):
		try :
			DBfile=open(self.filename, "a")
		except IOError:
			sys.exit()
		DBfile.write(data+"\n")
		DBfile.close()
		sys.stdout.write("item successfully added to database\n")
	def delate(self, data):
		try:
			DBfile=open(self.filename, 'r')
		except IOError:
			sys.exit()
		DBlist=DBfile.readlines()
		DBfile.close()
		#DBfile을 열고 모든 데이터를 리스트 하나에 저장
		#새로운 리스트 생성
		try:
			DBfile=open(self.filename, "w")
		except IOError:
			sys.exit()
		marker=False
		for item in DBlist:
			item=item.strip('\n')
			if item==data:
				marker=True
				continue
			DBfile.write(item+"\n")
		DBfile.close()
		if marker is True:
			sys.stdout.write("item successfully delated from database")
		else:
			sys.stdout.write("item is not in database or an error occured while delating item")
		sys.stdout.write("\n")
class databaseDictionary: #사전으로 이루어지는 데이터베이스(used in shellcodeDB)
	def __init__(self, DBfilename):
		self.filename=DBfilename
	def add(self, data):
		pass
	def delate(self, data):
		pass
class hexViewer:
	def __init__(self):
		self.filename=[]
		self.filedata=[]
		self.filedata_size=0;
		self.bufferSize=16
	def openFile(self, _filename):
		self.filename=_filename
		try:
			f=open(self.filename, "rb")
		except IOError:
			sys.exit()
		self.filedata=f.read()
		for data in self.filedata:
			data=data&0xFF
		self.filedata_size=os.path.getsize(self.filename)
		f.close()
	def viewCode(self):
		sys.stdout.write("[Offset]")
		for i in range(0, 6):
			sys.stdout.write(' ')
		sys.stdout.write("[Hex]")
		for i in range(0, (self.bufferSize-1)*3+2):
			sys.stdout.write(' ')
		sys.stdout.write("[Strings]\n")
		filedata_length=0;
		if self.filedata_size%self.bufferSize==0:
			filedata_length=self.filedata_size/self.bufferSize;
		else:
			filedata_length=(self.filedata_size/self.bufferSize)+1;
		offset=0; read=0
		for i in range(0, int(filedata_length)):
			sys.stdout.write("%010X | "%(offset))
			n=0; counter=0
			for j in range(read, read+self.bufferSize):
				if j==self.filedata_size:
					break
				if n%4==0 or n==0:
					sys.stdout.write(' ')
					counter+=1
				sys.stdout.write("%02X "%(self.filedata[j]))
				if n==self.bufferSize-1:
					sys.stdout.write(' ')
					counter+=1
				n+=1
			offset+=n;
			if (self.bufferSize*3+5)-(n*3+counter)>0:
				for j in range(0, (self.bufferSize*3+5)-(n*3+counter)):
					sys.stdout.write(' ')
				#sys.stdout.write(' ')
			sys.stdout.write('|')
			for j in range(read, read+self.bufferSize):
				try:
					if self.filedata[j]>=0x20 and self.filedata[j]<=0x7E:
						sys.stdout.write(chr(self.filedata[j]))
					else:
						sys.stdout.write('.')
				except IndexError:
					sys.stdout.write('.')
			read+=n;
			sys.stdout.write("\n")
	def findFlag(self, keyword):
		for i in range(0, len(self.filedata)):
			flagMarker=False; weight=0; startpoint=0
			#var startpoint saves the index of data where the flag-like strings start
			for j in range(0, len(keyword)):
				if j is 0:
					startpoint=i
				if chr(self.filedata[i+weight]) is not keyword[j]:
					break
				weight+=1
				if j is len(keyword)-1:
					flagMarker=True
			if flagMarker is not False:
				sys.stdout.write("	***!!FLAG-LIKE STRING DISCOVERED!!***")
				sys.stdout.write("\n	")
				j=startpoint
				for j in range(startpoint, self.filedata_size):
					if not(self.filedata[j]>=0x20 and self.filedata[j]<=0x7E):
						break;
					else:
						sys.stdout.write(chr(self.filedata[j]))
				sys.stdout.write("\n")
	def correctJpegData(self):
		for i in range(32, self.filedata_size):
			if self.filedata[i]==0x00 and self.filedata[i+1]==0xFF and self.filedata[i+2] is not 0x00:
				sys.stdout.write("found JPEG structure error!");
				sys.stdout.write(" %02X "%(self.filedata[i+2]))
				sys.stdout.write("is not 0x00 after 0x00 0xFF")
				sys.stdout.write("\n")
				try:
					f=open(self.filename, "wb")
				except IOError:
					sys.exit()
				self.filedata[i+2]=0
				for j in range(0, self.filedata_size):
					f.write(self.filedata[j])
				f.close()
				sys.stdout.write("data corrected!")
				sys.stdout.write("\n")
	'''
	def disableVbaPassword(self):
		for i in self.filedata:
			if ord(self.filedata[i]) is 0x44:
				if ord(self.filedata[i+1]) is 0x50:
					if ord(self.filedata[i+2]) is 0x42:
						self.filedata[i+2]=chr(0x78)
	'''
class Decoder:
	def caesar_cipher(self, data):
		key=0
		for i in range(0, 26):
			key=i; flag=data; tmp=0
			#var tmp for saving temporary data while calculating between char & int types
			for j in flag:
				if ord(j)>=ord('A') and ord(j)<=ord('Z'):
					tmp=ord(j)-ord('A')
					j=chr(tmp)
					if ord(j)+key<0:
						j+=26
					j=(ord(j)+key)%26
					j+=ord('A')
				if ord(j)>=ord('a') and ord(j)<=ord('z'):
					tmp=ord(j)-ord('A')
					j=chr(tmp)
					if ord(j)+key<0:
						j+=26
					j=(ord(j)+key)%26
					j+=ord('a')
			if searchFlag(flag) is not False:
				sys.stdout.write("flag found:")
				sys.stdout.write(flag)
				sys.stdout.write("\n")
			else:
				sys.stdout.write(flag)
				sys.stdout.write("\n")
os.system("cls")
#menu
sys.stdout.write("---Allyajyo---\n")
'''
sys.stdout.write("1. analyze file\n");
sys.stdout.write("2. encode / decode data\n");
sys.stdout.write("3. crawl webpage\n");
sys.stdout.write("or input other vaild Allyajyo commands\n")
'''
flagDB_filename="database/flagDB.txt" #flagDB의 경로
flagDB=database(flagDB_filename) #flagDB 선언 및 세팅
while 1:
	command=input("USER@Allyajyo : ")
	if command=="analyze" or command=="anal":
		file_name=input("file name to analyze : ")
		hexviewer=hexViewer()
		hexviewer.openFile(file_name)
		hexviewer.viewCode()
		try:
			DBfile=open(flagDB_filename, 'r')
		except IOError:
			sys.exit()
		DBlist=DBfile.readlines()
		DBfile.close()
		for item in DBlist:
			item=item.strip('\n')
			sys.stdout.write("<!--detecting for '%s' flag-like strings-->\n"%item)
			hexviewer.findFlag(item)
		if getFileExtension(file_name) is ".jpg" or ".jpeg":
			hexviewer.correctJpegData()
		'''
		if getFileExtension(file_name) is ".ppsm":
			hexviewer.disableVbaPassword()
		'''
	elif command=="2":
		data=input("data to decode : ")
		decoder=Decoder()
		#decoder.caesar_cipher(data)
	elif command=="3":
		sys.stdout.write("this feature is in development\n")
	elif command=="quit" or command=="exit" or command=="exit()":
		sys.exit()
	elif command=="add keyword" or command=="addkey":
		data=input("keyword to add in database : ")
		flagDB.add(data)
	elif command=="delate keyword" or command=="delkey":
		data=input("keyword to delate in database : ")
		flagDB.delate(data)
	else:
		sys.stdout.write("not a vaild command\n")
	sys.stdout.write("\n");
