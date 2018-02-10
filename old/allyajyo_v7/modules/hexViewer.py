import os
import sys
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
		self.filedata=bytearray(self.filedata)
		for i in range(32, self.filedata_size):
			if self.filedata[i]==0x00 and self.filedata[i+1]==0xFF and self.filedata[i+2]!=0x00:
				sys.stdout.write("found JPEG structure error!");
				sys.stdout.write(" %02X "%(self.filedata[i+2]))
				sys.stdout.write("is not 0x00 after 0x00 0xFF")
				sys.stdout.write("\n")
				try:
					f=open(self.filename, "wb")
					self.filedata[i+2]=0x00
					f.write(self.filedata)
					f.close()
					sys.stdout.write("data corrected!")
				except IOError:
					sys.stdout.write("cannot open file '%s'"%self.filename)
				sys.stdout.write("\n")
		self.filedata=bytes(self.filedata)
