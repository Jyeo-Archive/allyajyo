import os
import sys
def getExt(file_name):
	file_extenstion=os.path.splitext(file_name)[1]
	return file_extenstion
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
			filedata_length=self.filedata_index/self.bufferSize;
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
	def findFlag():
		pass
	def correctPngData():
		pass
os.system("cls")
file_name=raw_input("file name to analyze : ")
hexviewer=hexViewer()
hexviewer.openFile(file_name)
hexviewer.viewCode();
#hexviewer.findFlag();
#if GetFileExtenstion(file_name) is ".png":
	#hexviewer.correctPngData();

