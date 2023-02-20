from pyngrok import ngrok

def startNgrok():
    url = ngrok.connect(8090)
    print("Teeu > Full Url : ", url)
    print("Teeu > Tunnel Url : ", url.public_url)

def init():
    startNgrok()

init()