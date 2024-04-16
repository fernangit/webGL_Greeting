#https://aiacademy.jp/media/?p=57
#http://localhost:8000/
from flask import Flask, request
import datetime
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/StreamingAssets/Utterance', methods=['POST'])
def updateUtter():
    print('post')
    
    dt_now = datetime.datetime.now()
    
    filename = 'StreamingAssets/Utterance/utter.txt'
    utterance = request.form['utterance']
    print(filename)
    print(utterance)
    with open(filename, mode='w', encoding='utf-8') as fout:
        fout.write(utterance)

    filename = 'StreamingAssets/Utterance/score.txt'
    score = request.form['score']
    print(filename)
    print(score)
    with open(filename, mode='w', encoding='utf-8') as fout:
        fout.write(score)

    filename = 'StreamingAssets/Utterance/message.txt'
    message = request.form['message']
    print(filename)
    print(message)
    with open(filename, mode='w', encoding='utf-8') as fout:
        fout.write(message)
        
    filename = 'StreamingAssets/Utterance/response.txt'
    response = request.form['response']
    print(filename)
    print(response)
    with open(filename, mode='w', encoding='utf-8') as fout:
        fout.write(response)

    #chat log
    if message != '' and response != '':
        filename = 'StreamingAssets/Utterance/chatlog_' + str(dt_now.year).zfill(4) + str(dt_now.month).zfill(2) + str(dt_now.day).zfill(2) + '.txt'
        print(filename)
        if os.path.exists(filename):
            fout = open(filename, "a", encoding = "utf_8")
        else:
            fout = open(filename, "w", encoding = "utf_8")

        fout.write(dt_now.strftime('%Y/%m/%d %H:%M:%S') + ":mes:" + message + "\n")
        fout.write(dt_now.strftime('%Y/%m/%d %H:%M:%S') + ":res:" + response + "\n")

        fout.close()

    print('writed!')

    return utterance

def startServer(url, pnum):
    app.run(host=url, port=pnum, debug=True)

if __name__ == '__main__':
    startServer('localhost', 8000)
