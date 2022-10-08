import datetime as dt
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import requests.api
import websocket
from collections import deque
from sklearn.linear_model import LinearRegression
from threading import Thread
from time import sleep
from scipy.stats import norm

# initialize
is_open = True
BASE_URL = f'https://{apiserver_domain}/v2' # This is the base URL for paper trading
ACCOUNT_URL = f'{BASE_URL}/account'
DATA_URL = 'https://data.alpaca.markets/v2'
KEY = ''
keys = {'APCA-API-KEY-ID' : '', 'APCA-API-SECRET-KEY' : ''}
# connect and authenticate to regular
account = json.loads(requests.get(ACCOUNT_URL, headers=keys).content)
# print(account)
if not account['status'] == 'ACTIVE':
    exit(1)
# 1 = longing, 2 = shorting, 3 = hard shorting
prev_order = ''
# Prevent trying to trade before the previous trade is done
trading = False

def on_open(ws):
    print("opened")
    login = {'action': 'auth', 'key': f'{KEY}', 'secret': f'{SECRET}'}
    ws.send(json.dumps(login))
    # one-minute bars
    listen_message = {'action': 'subscribe', 'bars':['VIX']}
    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print(message)
    bar = json.loads(message)[0]
    avg = (bar['o'] + bar['l']) / 2
    if not trading:
        Thread(target=trade, args=("VXX", )).start()

def trade(symbol):
    print("top of trade")
    global trading
    trading = True
    r = requests.get(f"{BASE_URL}/account", headers=keys)
    # store cash for later
    cash = float(json.loads(r.text)['cash']) 
    print(f"cash: {cash}")
    # print("done checking on account...")
    
    # get vix price
    if is_open:
        global prev_order
        payload = {}
        r = requests.get(f"{DATA_URL}/stocks/{symbol}/bars", params=payload, headers=keys)
        # we now have a list of bars
        trading = False
        # change this as needed
        sleep(30)


def __main__():
    socket = "wss://stream.data.alpaca.markets/v2/iex"
    ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
    ws.run_forever()

if __name__ == '__main__':
    __main__()