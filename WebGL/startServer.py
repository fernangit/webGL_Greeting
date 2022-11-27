#https://aiacademy.jp/media/?p=57
#http://localhost:8000/
from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')

def startServer(pnum):
    app.run(port=pnum, debug=True)

if __name__ == '__main__':
    startServer(8000)