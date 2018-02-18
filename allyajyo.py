import os
import sys
#import base64
#import pefile
from modules import database
from modules import hexViewer
from modules import Decoder
from modules import visualizer
from modules import zipExtracter
def getFileExtension(file_name):
	file_extenstion=os.path.splitext(file_name)[1]
	return file_extenstion
os.system('cls')
#menu
sys.stdout.write('===Allyajyo===\n')
'''
sys.stdout.write('1. analyze file\n');
sys.stdout.write('2. encode / decode data\n');
sys.stdout.write('3. crawl webpage\n');
sys.stdout.write('or input other vaild Allyajyo commands\n')
'''
flagDB_filename='modules/database/flagDB.txt' #flagDB의 경로
flagDB=database.database(flagDB_filename) #flagDB 선언 및 세팅
while 1:
	command=input('USER@Allyajyo : ')
	if command=='analyze' or command=='anal':
		file_name=input('file name to analyze : ')
		hexviewer=hexViewer.hexViewer()
		hexviewer.openFile(file_name)
		hexviewer.viewCode()
		try:
			DBfile=open(flagDB_filename, 'r')
			DBlist=DBfile.readlines()
			DBfile.close()
			for item in DBlist:
				item=item.strip('\n')
				sys.stdout.write("<!--detecting for '%s' flag-like strings-->\n"%item)
				hexviewer.findFlag(item)
		except IOError:
			sys.stdout.write("cannot find database file '%s'\n"%flagDB_filename)
			sys.stdout.write('cannot search for flags\n')
		if getFileExtension(file_name) is '.jpg' or '.jpeg':
			hexviewer.correctJpegData()
	elif command=='decode':
		data=input('data to decode : ')
		decoder=Decoder.Decoder(data)
		decoder.base64()
	elif command=='3':
		sys.stdout.write('this feature is in development\n')
	elif command=='quit' or command=='exit' or command=='exit()' or command=='q' or command=='e':
		sys.exit()
	elif command=='add keyword' or command=='addkey':
		data=input('keyword to add in database : ')
		flagDB.add(data)
	elif command=='delate keyword' or command=='delkey':
		data=input('keyword to delate in database : ')
		flagDB.delate(data)
	elif command=='visualize' or command=='visual':
		file_name=input('file name to visualize : ')
		visualizer.visualizer(file_name)
	elif command=='zip':
		zip_file_name=input('zip file name to recover password : ')
		Zip=zipExtracter.zip(zip_file_name)
		sys.stdout.write('1. solve with dictionary\n2. solve with brue force\n')
		mode=int(input('choose recovery method : '))
		dicname=[]
		if mode==1:
			dicname=input('input dictionary file name : ')
		Zip.setmode(mode, dicname)
	else:
		sys.stdout.write('not a vaild command\n')
	sys.stdout.write('\n')
