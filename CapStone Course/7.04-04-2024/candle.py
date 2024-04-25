import yfinance as yf
import mplfinance as mpf

stock_symbol = 'AAPL'  # Example: Apple Inc.
stock_data = yf.download(stock_symbol, start='2024-02-22', end='2024-03-22')

mpf.plot(stock_data, type='candle', style='charles', title=f'{stock_symbol} Candlestick Chart',
         ylabel='Price', ylabel_lower='Volume', volume=True, show_nontrading=True)

mpf.show()