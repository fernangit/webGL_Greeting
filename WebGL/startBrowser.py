import webbrowser

#ブラウザ起動　画面MAX
def startBrowser(url):
    webbrowser.open(url, new=0, autoraise=True)
      
if __name__ == '__main__':
    startBrowser('http://localhost:8000/')
