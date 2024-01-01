import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 기간 설정 (1년)
start_date = pd.to_datetime('now') - pd.DateOffset(years=1)
end_date = pd.to_datetime('now')

# NASDAQ 상위 10개 종목 리스트
nasdaq_tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA', 'GOOG', 'PYPL', 'ADBE']

# 종목당 거래량 데이터 저장하는 데이터프레임
volume_df = pd.DataFrame()

# 각 종목에 대해 1년 동안의 거래량 데이터 가져오기
for ticker in nasdaq_tickers:
    try:
        # 1년 동안의 거래량 데이터 가져오기
        volume_data = yf.Ticker(ticker).history(start=start_date, end=end_date)['Volume']
        # 데이터프레임에 추가
        volume_df[ticker] = volume_data
    except Exception as e:
        print(f"Failed to fetch data for {ticker}: {e}")

# 각 종목별로 하위 10% 수준의 평균 계산
lower_10th_percentile_means = volume_df.quantile(0.1)

# 거래량 데이터를 시각화하여 비교
for ticker, volume in volume_df.items():
    plt.plot(volume, label=ticker)

# 각 종목별로 하위 10% 수준의 평균을 빨간색 점선으로 표시
for ticker, mean_value in lower_10th_percentile_means.items():
    plt.axhline(y=mean_value, linestyle='--', color='red', label=f'{ticker} Lower 10% Mean')

plt.title('Comparison of Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# 각 종목별로 하위 10% 수준의 평균 출력
print("\nLower 10th Percentile Means for Each Ticker:")
print(lower_10th_percentile_means)
