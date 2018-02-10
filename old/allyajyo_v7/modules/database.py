import sys
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
