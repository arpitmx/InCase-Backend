import os

from flask import *
import json, time
import pusher
from pynput.keyboard import *
import platform
import webbrowser

app = Flask(__name__)

pusher_client = pusher.Pusher(
  app_id='1556681',
  key='276c6bb8aeb296ca6dba',
  secret='b07905fc2f39b34a20ab',
  cluster='ap2',
  ssl=True
)

def tapAll(result, keyboard):
    time.sleep(2)
    for i in result:
        keyboard.tap(i)

@app.route('/request/', methods=['GET'])
def home_page():
    user_query = request.args.get("connect")
    print("> Connected to " + user_query + " Time :" + time.time())
    data_set = {'Page': 'Home', 'Message': 'Connect to ' + platform.platform(), 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump


# @app.route('/img/')
# def get_image():
#     if request.args.get('type') == '1':
#        filename = 'img.jpg'
#     else:
#        filename = 'img.jpg'
#     return send_file(filename, mimetype='image/gif')

def start(link):
    webbrowser.open(link)

def shutdown():
    os.system("shutdown -h now")


def notifyApp(msg,tone):
    pusher_client.trigger('sexy-channel69', 'sexy-event', {"message": msg, "tone": tone})

#https://88ca-2405-201-402d-7805-d063-72ab-e848-5413.in.ngrok.io/baachi/?mows=ring&?tone=1
@app.route('/baachi/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('mows'))
    ringtone = str(request.args.get('tone'))
    # /user/?query=User_Name

    print("User wrote : ",user_query)
    #data_set = {'Page': 'Request', 'Message': f'{result} ', 'Timestamp': time.time()}
    #json_dump = json.dumps(data_set)
    # webbrowser.open(result)
    #keyboard = Controller()
    #tapAll(result, keyboard)
    #start(result)
    #shutdown()
    notifyApp(user_query,ringtone)
    return f"baachi mows {user_query}"


@app.route('/')
def home():
    return "Fuck bitches 69"


if __name__ == '__main__':
    app.run(port=8080, debug= True)


