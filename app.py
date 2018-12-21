import os
import requests
from flask import Flask, request
app = Flask(__name__)

token = os.getenv('TELEGRAM_BOT_TOKEN')

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route(f'/{token}',methods=['POST'])
def telegram():
    #1. 구조 확인하기
    from_telegram = request.get_json()          #> dict form
    print(from_telegram)
    
    #2 그대로 돌려보내기(메아리 챗봇)
    #['message'] >> 키가 없으면 에러 生
    #.get('messge')  >> 키가 없으면, None 반한, 에러x
    if from_telegram.get('message') is not None:
        chat_id = from_telegram['message']['chat']['id']
        text = from_telegram['message']['text']
        requests.get(f'https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text={text}')   #ap.telegram.org 는 막혀서 api.hphk.io/telegram 로 변경
   
    return '', 200
    
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))