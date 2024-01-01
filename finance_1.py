import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

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

# 결과를 담을 데이터프레임 초기화
result_df = pd.DataFrame()

for ticker in nasdaq_tickers:
    # 주식의 2022년 데이터 가져오기
    stock = yf.Ticker(ticker)
    start_date = '2021-01-01'
    end_date = '2023-12-20'
    stock_data = stock.history(start=start_date, end=end_date)

    # 날짜와 종가만을 가지는 데이터프레임 생성
    stock_df = pd.DataFrame({
        'Date': stock_data.index.date,  # 날짜를 년, 월, 일로만 저장
        f'{ticker} Close Price': stock_data['Close']
    })

    # 고점 대비 오늘의 가격 차이 계산
    max_price_date = stock_data['Close'].idxmax()
    max_price = stock_data['Close'].max()
    today_price = stock_data['Close'].iloc[-1]
    percentage_change = ((today_price - max_price) / max_price) * 100

    # 등락율이 -15% 이상인 종목만 필터링하여 결과 데이터프레임에 추가
    if percentage_change <= -15:
        result_df = pd.concat([result_df, stock_df], axis=1)

        # 종목별 결과 출력
        print(f'{ticker} 고점일: {max_price_date.strftime("%Y-%m-%d")}, 고점가: {max_price}')
        print(f'{ticker} 오늘({stock_data.index[-1].strftime("%Y-%m-%d")}) 종가: {today_price}')
        print(f'{ticker} 고점 대비 가격 차이: {percentage_change:.2f}%\n')

# 전체 결과 출력
result_file_path = 'stock_prices_and_changes_filtered.csv'
result_df.to_csv(result_file_path, index=False)
print(f'등락율이 -15% 이상인 종목의 주가 데이터를 {result_file_path}에 저장했습니다.')
