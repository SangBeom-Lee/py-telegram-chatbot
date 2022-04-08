import urllib.request
import urllib.parse
import json
import time
import Character

## 토큰
TOKEN           = '1035201823:AAFG0lwnbWyPDHypg5xQxyw3y3-6RNlZaEQ'

## 리퀘스트
def request(url):
    response    = urllib.request.urlopen(url)
    byte_data   = response.read()
    text_data   = byte_data.decode()

    return text_data

## 요청 URL 생성함수
def build_url(method, query):
    return      f'https://api.telegram.org/bot{TOKEN}/{method}?{query}'

## 객체변환
def request_to_chatbot_api(method, query):
    url         = build_url(method, query)
    response    = request(url)
    
    return json.loads(response)

## 필요한 정보 추출
def simplify_messages(response):
    result                  = response['result']
    if not result:
        return None, []
    
    last_update_id          = max(item['update_id'] for item in result)
    messages                = [item['message'] for item in result]
    simplified_messaages    = [{
        'from_id'   : message['from']['id'],
        'text'      : message['text']}
        for message in messages
    ]

    return last_update_id, simplified_messaages

## 확인 후 결과 추출 함수
def get_updates(update_id):
    query       = f'offset={update_id}'
    response    = request_to_chatbot_api(method='getUpdates', query=query)

    return simplify_messages(response)

## 메시지 발송
def send_message(chat_id, text):
    text        = urllib.parse.quote(text)
    query       = f'chat_id={chat_id}&text={text}'
    response    = request_to_chatbot_api(method='sendMessage', query=query)

    return response
    
## 확인 후 발송
def check_messages_and_response(next_update_id):
    last_update_id, recieved_messages   = get_updates(next_update_id)

    for message in recieved_messages:
        chat_id     = message['from_id']
        text        = message['text']
        send_text   = Character.textVerfiCation(text)

        send_message(chat_id, send_text)

    return last_update_id



if __name__ == '__main__':
    try:
        with open('last_update_id.txt', 'r') as file:
            next_update_id  = int(file.read())
    except (FileNotFoundError, ValueError):
        next_update_id      = 0

    while True:
        last_update_id      = check_messages_and_response(next_update_id)

        if last_update_id:
            next_update_id  = last_update_id + 1
        
        time.sleep(5)