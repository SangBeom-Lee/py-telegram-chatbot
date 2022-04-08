import urllib.request
import urllib.parse
from datetime import datetime

## 문자 답변 가져오기
def textVerfiCation(text):
    send_message            = ""

    if text == "야":
        send_message        = "왜"
    elif "몇시" in text:
        now                 = datetime.now()
        nowTime             = now.hour
        nowMinute           = now.minute
        if "지금" in text:
            send_message    = f"현재 시각 {nowTime}시 {nowMinute}분 입니다.\n시간을 봐 새끼야"
        else :
            send_message    = f"현재 시각 {nowTime}시 {nowMinute}분 입니다.\n시간을 봐 새끼야"
    elif "몇일" in text:
        now                 = datetime.now()
        nowMonth            = now.month
        nowDay              = now.day

        if "오늘" in text:
            send_message    = f"오늘은 {nowMonth}월 {nowDay}일 입니다."
        elif "내일" in text: 
            nowDay          = now.day+1
            send_message    = f"내일은 {nowMonth}월 {nowDay}일 입니다."
        else :
            send_message    = f"오늘은 {nowMonth}월 {nowDay}일 입니다."
    elif "안녕" in text:
        send_message        = "반갑습니다. 이상범님의 도구 여러분"
    ## 욕 거르기함수
    elif "씨발" in text or "좆" in text:
        send_message        = getSwear(text)
    else :
        send_message        = "현재 적용된 기능이 아닙니다.\n기능이 확장되기를 기다리세요."

    return send_message

## 욕 거르기
def getSwear(send_message):
    message                 = ""

    if "씨발" in send_message:
        message             += "씨발?\n"
    if "좆" in send_message:
        message             += "좆?\n"

    message                 += "욕하지마라\n씨발년아 경고한다."

    return message