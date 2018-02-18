import sys
import base64
class Decoder: #디버깅 중에 있음
	def __init__(self, data):
		self.data=data
	def base64(self):
		flag=base64.b64decode(bytes(self.data, 'UTF-8')).decode()
		sys.stdout.write('result decoded by base64 : '+flag+'\n')
