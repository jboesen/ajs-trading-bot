import vectorbt as vbt
import plotly.graph_objs as go 

vbt.settings.data['alpaca']['key_id'] = 'PKFTNP8WTF3YNWNIPH6R'
vbt.settings.data['alpaca']['secret_key'] = 'Y7MURXQa2qzFanfwHuhmty2hLxfNsEj2kSjfzqkO'

alpacadata = vbt.AlpacaData.Download(symbol='AAPL', start='4 days ago UTC`, end=`1 day ago UTC`, timeframe='1h')

alpaca.get_data()
plotly.g


fast_ma = vbt.MA.run(alpacadata, 10, short_name='fast')
slow_ma = vbt.MA.run(alpacadata, 20, short_name='slow')

entries = fast_ma.ma_crossed_above(slow_ma)
entries
