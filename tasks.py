from microsoftbotframework import ReplyToActivity
import requests
import json
import socket 

def echo_response(message):
  print(message)
  
  if message["type"] == "message":
    if "카드" in message["text"]:
      print(message["from"])
      msg = "카드 서비스 준비 중 입니다."
    elif "비교" in message["text"]:
      msg = "비교 서비스 준비 중 입니다."
    elif "안녕" in message["text"]:
      msg = "안녕하세요."
    else:
      msg = "응답할 수 없음"
  
    s = socket.socket()
    # host = '13.124.234.183'
    host = '222.106.22.63'
    port = 12222

    s.connect((host, port))
    print('Connected to', host)

    #send_msg = input("Enter something for the server: ")
    send_msg = message["text"]
    s.send(send_msg.encode('utf-8'))
    # Halts
    print('[Waiting for response...]')
    recv_msg = s.recv(1024).decode('utf-8')
    print(recv_msg)
    s.close()
    ReplyToActivity(fill=message, text=recv_msg).send()
