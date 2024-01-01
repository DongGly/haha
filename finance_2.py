import yfinance as yf

# NASDAQ 상위 100개 종목 리스트
nasdaq_tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'TSLA', 'NVDA', 'GOOG', 'PYPL', 'ADBE',
               'NFLX', 'INTC', 'CMCSA', 'PEP', 'CSCO', 'COST', 'AMGN', 'TMUS', 'AVGO', 'TXN',
               'QCOM', 'CHTR', 'SBUX', 'MDLZ', 'INTU', 'ISRG', 'GILD', 'BKNG', 'AMAT', 'ADP',
               'VRTX', 'CSX', 'ATVI', 'MU', 'ADSK', 'BIIB', 'ILMN', 'AMD', 'REGN', 'LRCX', 'FISV',
               'JD', 'ADI', 'NXPI', 'KHC', 'EBAY', 'BIDU', 'MELI', 'MNST', 'KLAC', 'WDC', 'DOCU',
               'ASML', 'EXC', 'IDXX', 'ALGN', 'CTSH', 'SPLK', 'EA', 'DXCM', 'NTES', 'WDAY', 'ZM',
               'SNPS', 'CDNS', 'MRNA', 'XEL', 'ORLY', 'ANSS', 'CPRT', 'MAR', 'CTAS', 'FAST', 'DLTR',
               'ROST', 'SGEN', 'INCY', 'VRSN', 'CERN', 'SIRI', 'ALXN', 'TTWO', 'CHKP', 'SWKS', 'MXIM',
               'ULTA', 'TTD', 'LULU', 'AEP', 'WBA', 'MTCH', 'PCAR', 'MCHP', 'PAYX', 'FOXA', 'FOX',
               'OKTA', 'CDW', 'TCOM', 'CSGP', 'XLNX', 'PTON', 'BMRN', 'EXPE', 'CTXS', 'VRSK', 'NTAP',
               'BLL', 'NLOK', 'MKTX', 'GLPI']
print(len(nasdaq_tickers))
nasdaq_tickers_noData = []
tickers_to_remove = []

for ticker in nasdaq_tickers:
    stock_data = yf.Ticker(ticker).history(period='1d')
    if stock_data.empty:
        print(f'{ticker}: No data found')
        nasdaq_tickers_noData.append(ticker)
        tickers_to_remove.append(ticker)
    else:
        print(f'{ticker}: Data exists')

# 데이터가 없는 티커 제거
for ticker in tickers_to_remove:
    nasdaq_tickers.remove(ticker)

# 최종적으로 업데이트된 티커 리스트와 데이터가 없는 티커 리스트 출력
print("Updated NASDAQ Tickers:", nasdaq_tickers)
print(len(nasdaq_tickers))
print("Tickers with no data:", nasdaq_tickers_noData)
print(len(nasdaq_tickers_noData))


# # 각 종목에 대한 정보를 저장할 리스트
# stock_info = []
#
# # 각 종목에 대한 정보를 가져옴
# for stock in nasdaq_tickers:
#     data = yf.Ticker(stock)
#     stock_info.append(data.info)
#
# # 결과 출력
# for info in stock_info:
#     print(info)

