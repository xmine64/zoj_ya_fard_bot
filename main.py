import os
import requests

from datetime import datetime, timedelta

#
# configurations
#

# date of starts of classes
start = datetime(int(os.environ['START_YEAR']), int(os.environ['START_MONTH']), int(os.environ['START_DAY']))
# telegram bot token
tokenId = os.environ['BOT_TOKEN_ID']
# target channel id
chatId = os.environ['CHAT_ID']
# messages
evenText = "فردا هفته زوجه"
oddText = "فردا هفته فرده"

#
# functions
#

def isEven(start: datetime, current: datetime) -> bool:
    # difference of days since start of classes
    days = (current - start).days
    # current week number
    weeks = int(days) + 1
    # if weeks is divisible by 2 then it's even week, else it's odd week
    return (weeks%2) == 0

def send(tokenId, chatId, message):
    url = "https://api.telegram.org/bot%s/sendMessage" % tokenId
    params = { 'chat_id': chatId, 'text': message }
    requests.post(url = url, params = params)

message = evenText if isEven(start, datetime.now() + timedelta(days = 1)) else oddText
send(tokenId, chatId, message)