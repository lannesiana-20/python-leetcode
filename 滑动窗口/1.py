import pandas_datareader.data as data
# 获取纳斯达克股票符号列表
all_ticker = data.DataReader("AAPL", "yahoo", start="2023-01-01", end="2023-12-31")

# 查看数据基本信息
print(all_ticker.info())

# 查看前5行数据
print("\n前5行数据：")
print(all_ticker.head(5))