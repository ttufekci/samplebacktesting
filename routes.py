# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Make sure to read the docs about routes if you haven't already:
# https://docs.jesse.trade/docs/routes.html
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from jesse.utils import anchor_timeframe

# trading routes
routes = [
    ('Binance', 'BTCUSDT', '4h', 'MacdCrossStrategy'),
]

# in case your strategy requires extra candles, timeframes, ...
extra_candles = [
    ('Binance', 'BTCUSDT', anchor_timeframe('4h')),
]
