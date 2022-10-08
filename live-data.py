import websocket, json
from trade import trade
from queue import Queue

KEY = ''
SECRET = ''
current_price = Queue(maxsize = 10)
def on_open(ws):
    print("opened")
    login = {'action': 'auth', 'key': f'{KEY}', 'secret': f'{SECRET}'}
    ws.send(json.dumps(login))
    # one-minute bars
    listen_message = {'action': 'subscribe', 'bars':['VXX']}
    ws.send(json.dumps(listen_message))

def on_message(ws, message):
    pass

socket = "wss://stream.data.alpaca.markets/v2/iex"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=trade)
ws.run_forever()