#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import shutil
import random
import urllib.parse
from music_player import *
from visualizer import *
from flask import Flask, render_template, request, json
from threading import Thread

# def append_tags(playlist, playlist_tags):
#     for music in playlist:
#         music_tags = get_music_tags(music)
#         playlist_tags.append(music_tags)

app = Flask(__name__)
# global playlist
# playlist = get_playlist()

@app.route('/playlist')
def playlist():
    # 플레이리스트 
    playlist = get_playlist()
    # print(playlist)
    for idx, music in enumerate(playlist):
        music = music.replace('\\', '\\\\')
    # print(playlist)
    gradients = ['FC354C', '0ABFBC', 'fff132', '89253e', '#2c3e50']
    random.shuffle(gradients)
    return render_template(
        'music-player/playlist.html',
        playlist = playlist,
        music_path = music_path(),
        colors = gradients
    )

@app.route('/play/<path:musicfile>')
def music_play(musicfile):
    # 요청받은 음악 파일 경로의 음악 파일을 재생
    # 양 옆 버튼 누르면 페이지 reload
    tempDir = './webserver/static/temp/'
    list( map( os.unlink, (os.path.join(tempDir,f) for f in os.listdir(tempDir)) ) )
    music = musicfile
    music_tags = get_music_tags(music)
    print(music_path())
    temp_file = tempDir + os.path.basename(music)
    shutil.copy(music, temp_file)
    temp_file = temp_file.replace('./webserver/static/', '')
    # replace_path = music_path() + '\\'
    return render_template(
        'music-player/index.html', 
        music_name = temp_file, 
        tags = music_tags
    )

@app.route("/music-random")
def music_play_random():
    # 사용자의 <음악> 폴더에서 랜덤 음악 하나를 재생 
    # 음악 하나만 가져오고, 양 옆 버튼 누르면 페이지 reload
    tempDir = './webserver/static/temp/'
    list( map( os.unlink, (os.path.join(tempDir,f) for f in os.listdir(tempDir)) ) )
    music = get_random_music()
    print(music)
    music_tags = get_music_tags(music)
    temp_file = tempDir + music.replace(music_path() + '\\', '')
    shutil.copy(music, temp_file)
    # replace_path = music_path() + '\\'
    temp_file = temp_file.replace('./webserver/static/', '')
    return render_template(
        'music-player/index.html', 
        music_name = temp_file, 
        tags = music_tags
    )

@app.route("/file-analysis", methods=['GET'])
def file_analysis():
    filename = request.args.get('file')
    # print (os.getcwd()) # C:\Users\JunhoYeo\Documents\allyajyo-electron 기준
    f=open(filename, 'rb')
    filedata = f.read()
    for data in filedata:
        data = data & 0xFF
    filedata_size = os.path.getsize(filename)
    visualizedImageName = visualize(filename)
    
    # filedata를 처리 => offset(오프셋 값), hexcode(헥스코드), string(문자열)
    # sys.stdout.write('[Offset]')
	# for i in range(0, 6):
	# 	sys.stdout.write(' ')
	# sys.stdout.write('[Hex]')
	# for i in range(0, (bufferSize-1)*3+2):
	# 	sys.stdout.write(' ')
	# sys.stdout.write('[Strings]\n')
    bufferSize = 16
    hexviewerData_offset_line = []
    hexviewerData_hexcode_line = []
    hexviewerData_string_line = []
    filedata_length=0;
    if filedata_size%bufferSize==0:
    	filedata_length=filedata_size/bufferSize;
    else:
    	filedata_length=(filedata_size/bufferSize)+1;
    offset=0; read=0
    hexviewerData_line = int(filedata_length);
    for i in range(0, int(filedata_length)):
        # hexviewerData_offset = []
        # hexviewerData_string = []
        hexviewerData_offset_line.append('%010X'%(offset))
        n=0; counter=0
        hexviewerData_hexcode = []
        for j in range(read, read+bufferSize):
            if j==filedata_size:
                break
            if n%4==0 or n==0:
                # sys.stdout.write(' ')
                counter+=1
            hexviewerData_hexcode.append('%02X'%(filedata[j]))
            if n==bufferSize-1:
                # sys.stdout.write(' ')
                counter+=1
            n+=1
        offset+=n;
        # if (bufferSize*3+5)-(n*3+counter)>0:
        # 	for j in range(0, (bufferSize*3+5)-(n*3+counter)):
        # 		sys.stdout.write(' ')
        #sys.stdout.write(' ')
        # sys.stdout.write('|')
        hexviewerData_string_temp = ''
        for j in range(read, read+bufferSize):
            try:
                if filedata[j]>=0x20 and filedata[j]<=0x7E:
                    hexviewerData_string_temp += (chr(filedata[j]))
                else:
                    hexviewerData_string_temp += ('.')
            except IndexError:
                hexviewerData_string_temp += ('.')
        read+=n;
        hexviewerData_string_line.append(hexviewerData_string_temp)
        # sys.stdout.write('\n')
        # hexviewerData_offset_line.append(hexviewerData_offset)
        hexviewerData_hexcode_line.append(hexviewerData_hexcode)
        # hexviewerData_string_line.append(hexviewerData_string)
    # print(hexviewerData)
    # print(hexviewerData_offset_line)
    # print(hexviewerData_hexcode_line)
    # print(hexviewerData_string_line)
    # hexviewerData_offset_line = json.dumps(hexviewerData_offset_line)
    # print(hexviewerData_offset_line)
    return render_template(
        'file-analyzer/index.html',
        # filedata_length = hexviewerData_line,
        filedata_offset = hexviewerData_offset_line,
        filedata_hexcode = hexviewerData_hexcode_line,
        filedata_string = hexviewerData_string_line
    )

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=5000)