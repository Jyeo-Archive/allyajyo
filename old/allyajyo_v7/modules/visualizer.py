import sys
def visualizer(filename):
	try: #from PIL import Image를 시도, Pillow 설치 여부를 확인
		from PIL import Image
		image=Image.new("RGB", (256, 256))
		try: #file open 시도
			f=open(filename, "rb")
			filedata=f.read()
			for data in filedata:
				data=data&0xFF
			f.close()
			for i in range(0, len(filedata)-1):
				image.putpixel((filedata[i+1], filedata[i]), (255, 255, 255))
			filename=filename.strip('\n')
			filename=filename.replace('.', '_')
			image.save("visualized_"+filename+".png")
			sys.stdout.write("image successfully visualized and saved as '%s'\n"%("visualized_"+filename+".png"))
		except IOError: #file open 실패
			sys.stdout.write("file not found\n")
	except ImportError: #Pillow 모듈이 설치되어 있지 않은 경우
		sys.stdout.write("Install Python module Pillow by running \'pip install pillow\' on terminal\n")
