from microsoftbotframework import ReplyToActivity
import requests
import json
import socket 
import sys 

def echo_response(message):
  print(message)
  if message["type"] == "message":
    if "카드" in message["text"]:
      msg = "카드 서비스 준비 중 입니다."
    elif "비교" in message["text"]:
      msg = "비교 서비스 준비 중 입니다."
    elif "안녕" in message["text"]:
      msg = "안녕하세요."
    else:
      msg = "응답할 수 없음"
      
    serverIP = '52.79.99.215'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # SOCK_STREAM은 TCP socket을 뜻함 
    # sock.bind((bindIP, 1)) 
    try: 
      sock.connect((serverIP, 12222)) 
    # 서버에 연결 요청 
    # 서버로 송신 
      sbuff = bytes(msg, encoding='utf-8') 
      sock.send(sbuff) # 메시지 송신 
      print('송신 {0}'.format(msg)) # 서버로부터 수신 
      rbuff = sock.recv(1024) # 메시지 수신 
      received = str(rbuff, encoding='utf-8') 
      print('수신 : {0}'.format(received)) 
    finally: socket.close()
      
    ReplyToActivity(fill=message, text=msg).send()
