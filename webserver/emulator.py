#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, requests

class chatbotEmulator:
    def __init__(self, _server_url, _user_key='JunhoYeo-Emulator'):
        self.user_key = _user_key
        if not _server_url[:7] == 'http://':
            _server_url = 'http://' + _server_url
        self.SERVER_URL = _server_url
        # get user_key, chatbot server url

        print('[*] user_key : ' + self.user_key)
        print('[*] SERVER_URL : ' + self.SERVER_URL)
        # log on console
    
    def sendMessage(self, message): # 메세지를 보내고 응답을 리턴
        # try:
        payload = {'user_key': self.user_key, 'type': 'text', 'content': message}
        r = requests.get(self.SERVER_URL + '/message', json=payload)
        # print(r.text)
        # print(type(r.text))
        res = json.loads(r.text[1:])
            # request for '/keyboard' and get request
        # except: 
            # print('[!] Error while requesting message.php with json payload')
            # exit() 
        print('[*] sucessfully recived response')
        print(str(res) + '\n')
        return res # return recived json response

    def getDefaultKeyboard(self): # 기본값 키보드를 가져옴 
        try: 
            r = requests.get(self.SERVER_URL + '/keyboard')
            r.encoding = 'utf-8'
            res = json.loads(r.text[3:])
            # request for '/keyboard' and get request
        except: 
            print('[!] Error while requesting keyboard.php')
            exit() 
        print('[*] sucessfully recived response')
        print(str(res) + '\n')
        # {
        #     "type": "buttons",
        #     "buttons": ["대화 시작"]
        # }
        # example response of keyboard.php
        return   json.loads(('{ \'keyboard\' : ' + str(res) + ' }').replace('\'', '\"'))

    def getKeyboardFromJSON(self, recv_json):
        keyboard_type = None
        try:
            print('[*] keyboard_type : ' + recv_json['keyboard']['type']) # log keyboard type on console
            keyboard_type = recv_json['keyboard']['type']
        except KeyError:
            print('[*] keyboard_type : text')
            keyboard_type = 'text'
        if keyboard_type == 'buttons': # button type keyboard
            return recv_json['keyboard']['buttons']
        else: # text type keyboard
            return 'text'

import ast
from flask import Flask, redirect, render_template, request, url_for, Blueprint

kakao_chatbot_emulator = Blueprint('kakao_chatbot_emulator', __name__, template_folder='templates/kakao-chatbot-emulator')
global chatbot
chatbot = None

@kakao_chatbot_emulator.route('/')
def home():
    return render_template('index.html')

@kakao_chatbot_emulator.route('/get-default', methods=['GET'])
def process_default():
    url = request.args.get('url')
    if url == '': 
        return redirect(url_for('kakao_chatbot_emulator.home'))
    global chatbot
    chatbot = chatbotEmulator(url)
    keyboard_json = chatbot.getDefaultKeyboard()
    keyboard = chatbot.getKeyboardFromJSON(keyboard_json)
    if keyboard == 'text': # text type keyboard
        return redirect(url_for('kakao_chatbot_emulator.text', json_recv=keyboard_json))
    else: # button type keyboard
        return redirect(url_for('kakao_chatbot_emulator.buttons', json_recv=keyboard_json, buttons=str(keyboard)))

@kakao_chatbot_emulator.route('/get-input', methods=['GET'])
def process_input():
    message = request.args.get('message')
    if message == '': 
        return redirect(url_for('kakao_chatbot_emulator.home'))
    global chatbot
    recv = chatbot.sendMessage(message)
    keyboard = chatbot.getKeyboardFromJSON(recv)
    message = None
    if keyboard == 'text': # text type keyboard
        return redirect(url_for('kakao_chatbot_emulator.text', json_recv=recv))
    else: # button type keyboard
        return redirect(url_for('kakao_chatbot_emulator.buttons', json_recv=recv, buttons=str(keyboard)))

@kakao_chatbot_emulator.route('/buttons', methods=['GET'])
def buttons():
    keyboard_json = request.args.get('json_recv')
    keyboard = request.args.get('buttons')
    keyboard = ast.literal_eval(keyboard)
    return render_template('buttons.html', json_recv=keyboard_json, buttons=keyboard)

@kakao_chatbot_emulator.route('/text', methods=['GET'])
def text():
    keyboard_json = request.args.get('json_recv')
    return render_template('text.html', json_recv=keyboard_json)

if __name__=='__main__':
    url = input('[-] input chatbot server url : ')
    chatbot = chatbotEmulator(url)
    keyboard = chatbot.getDefaultKeyboard()
    keyboard = chatbot.getKeyboardFromJSON(keyboard)
    message = None
    if keyboard == 'text': # 텍스트형 키보드
        message = input('[-] input message to send : ')
    else: # 버튼형 키보드
        print (keyboard)
        print('[+] select button')
        for idx, button in enumerate(keyboard):
            print(' [' + str(idx) + '] [ ' + button + ' ]')
            # print buttons 
        while True:
            select_index = input('[-] select button with index(q to quit) : ')
            if select_index == 'q' or select_index == 'quit':
                exit()
            try:
                message = keyboard[int(select_index)]
                break
            except IndexError:
                print('[!] Wrong index. Select again')    
    print('[*] message : ' + str(message) + '\n')
    recv = chatbot.sendMessage(message)

    while True:
        # print(message)
        keyboard = chatbot.getKeyboardFromJSON(recv)
        message = None
        if keyboard == 'text': # 텍스트형 키보드
            message = input('[-] input message to send : ')
        else: # 버튼형 키보드
            print('[+] select button')
            for idx, button in enumerate(keyboard):
                print(' [' + str(idx) + '] [ ' + button + ' ]')
                # print buttons 
            while True:
                select_index = input('[-] select button with index(q to quit) : ')
                if select_index == 'q' or select_index == 'quit':
                    exit()
                try:
                    message = keyboard[int(select_index)]
                    break
                except IndexError:
                    print('[!] Wrong index. Select again')    
        print('[*] message : ' + str(message) + '\n')
        recv = chatbot.sendMessage(message)
