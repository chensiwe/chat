import websocket
import redis
red=redis.Redis(host='127.0.0.1',port=6379,db='2')
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
        i=1
        while True:
            msg=red.rpop('msg')
            #print(msg,type(msg))
            if msg:
                print('have msg..........')
                ws.send("admin %s" % msg.decode('utf-8'))
            else:
                pass
            #t222ime.sleep(1)


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:10083",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
