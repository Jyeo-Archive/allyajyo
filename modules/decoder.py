import sys
class Decoder: #디버깅 중에 있음
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
