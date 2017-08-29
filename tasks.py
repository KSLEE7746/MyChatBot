from microsoftbotframework import ReplyToActivity
import requests
import json

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
      msg = "명령어 - 카드, 비교, 안녕"

    ReplyToActivity(fill=message, text=msg).send()
