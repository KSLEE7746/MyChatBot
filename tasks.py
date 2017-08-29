from microsoftbotframework import ReplyToActivity
import requests
import json
from konlpy.tag import Twitter
from konlpy.tag import Komoran

komoran = Komoran()

def konlpy_parse(text):
  return komoran.nouns(text)

def echo_response(message):
  print(message)
  
  if message["type"] == "message":
    print(konlpy_parse(message["type"]))
    if "카드" in message["text"]:
      msg = "카드 서비스 준비 중 입니다."
    elif "비교" in message["text"]:
      msg = "비교 서비스 준비 중 입니다."
    elif "안녕" in message["text"]:
      msg = "안녕하세요."
    else:
      msg = "응답할 수 없음"

    ReplyToActivity(fill=message, text=msg).send()
