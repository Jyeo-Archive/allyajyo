import os
import sys
import base64
def getFileExtension(file_name):
	file_extenstion=os.path.splitext(file_name)[1]
	return file_extenstion
def searchFlag(data):
	keyword="flag{" #must change this to reading keywords from file
	flagMarker=0
	for i in range(0, len(data)):
		weight=0; startpoint=0
		#var startpoint saves the index of data where the flag-like strings start
		for j in range(0, len(keyword)):
			if j is 0:
				startpoint=i
			if data[i+weight] is not keyword[j]:
				break
			weight+=1
			if j is len(keyword)-1:
				flagMarker=1
		if flagMarker!=0:
			return startpoint
		else:
			return False
		#this function returns the value of startpoint if flag-like strings were found
		#or False if no flags were found
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
			data=ord(data)&0xFF
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
		for i in range(0, filedata_length):
			sys.stdout.write("%010X | "%(offset))
			n=0; counter=0
			for j in range(read, read+self.bufferSize):
				if j==self.filedata_size:
					break
				if n%4==0 or n==0:
					sys.stdout.write(' ')
					counter+=1
				sys.stdout.write("%02X "%(ord(self.filedata[j])))
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
					if ord(self.filedata[j])>=0x20 and ord(self.filedata[j])<=0x7E:
						sys.stdout.write(self.filedata[j])
					else:
						sys.stdout.write('.')
				except IndexError:
					sys.stdout.write('.')
			read+=n;
			sys.stdout.write("\n")
	def findFlag(self):
			startpoint=searchFlag(self.filedata)
			if startpoint is not False:
				sys.stdout.write("***!!FLAG-LIKE STRING DISCOVERED!!***")
				sys.stdout.write("\n")
				for j in range(startpoint, self.filedata_size):
					if not(self.filedata[j]>=0x20 and self.filedata[j]<=0x7E):
						sys.stdout.write("error");
						break;
					elif self.filedata[j]=='{' or self.filedata[j]=='}' or self.filedata[j]=='_':
						sys.stdout.write(self.filedata[j])
					else:
						sys.stdout.write(self.filedata[j])
					sys.stdout.write("\n")
			else:
				sys.stdout.write("no flag-like strings found\n")
	def correctJpegData(self):
		for i in range(32, self.filedata_size):
			if self.filedata[i]==0x00 and self.filedata[i+1]==0xFF and self.filedata[i+2] is not 0x00:
				sys.stdout.write("found JPEG structure error!");
				sys.stdout.write(" %02X "%(ord(self.filedata[i+2])))
				sys.stdout.write("is not 0x00 after 0x00 0xFF")
				sys.stdout.write("\n")
				try:
					f=open(self.filename, "wb")
				except IOError:
					sys.exit()
				self.filedata[i+2]=0x00
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
sys.stdout.write("1. analyze file\n");
sys.stdout.write("2. encode / decode data\n");
sys.stdout.write("3. crawl webpage\n");
sys.stdout.write("or input other vaild Allyajyo commands\n")
while True:
	choice=raw_input("USER@Allyajyo : ")
	if choice is "1":
		file_name=raw_input("file name to analyze : ")
		hexviewer=hexViewer()
		hexviewer.openFile(file_name)
		hexviewer.viewCode()
		hexviewer.findFlag()
		if getFileExtension(file_name) is ".jpeg":
			hexviewer.correctJpegData()
		'''
		if getFileExtension(file_name) is ".ppsm":
			hexviewer.disableVbaPassword()
		'''
	if choice is "2":
		data=raw_input("data to decode : ")
		decoder=Decoder()
		decoder.caesar_cipher(data)
	if choice is "3":
		sys.stdout.write("this feature is in development\n")
	if choice is "quit" or "exit" or "exit()":
		sys.exit()
	sys.stdout.write("\n");
