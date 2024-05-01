#1. 從TEJ 或 Yahoo Finance 挑10檔股票，下載2020-2023年後的日資料，分別存成csv檔 (如2330.csv)，上傳到GitHub 
#2. 利用迴圈或函式下載小組成員GitHub上所有的股票 將執行後的.ipynb檔上傳到GitHub，

#1
#pip install yfinance
import yfinance as yf
import csv
import pandas as pd


stock=['3231.TW','5871.TW','2449.TW','2330.TW','2371.TW',
       '2363.TW','2324.TW','1504.TW','4915.TW','1609.TW']
data=[]

for i in range(len(stock)):
    df = yf.download(stock[i],start='2020-01-01',end='2023-12-31')
    data.append(df)
    print("stock_number=",stock[i])
    print(df)
    file_path = f"C:/Users/sunny/Desktop/financial applied/輸出csv/{stock[i]}.csv"
    data[i].to_csv(file_path,header=True)
   

#--Github下載
download = ["1225.TW","1234.TW","1235.TW","1301.TW","1303.TW",
            "1617.TW","2002.TW","2101.TW","2201.TW","2882.TW"]

base_url= "https://raw.githubusercontent.com/richie99999/fin_data/main/"

import pandas as pd
import io
import requests

for i in range (len(stock)):
    url = base_url + f"{download[i]}.csv"
    response = requests.get(url)
    if response.status_code == 200:
        squirrel = pd.read_csv(io.StringIO(response.text))
        print("\nstock number = ", download[i])
        print(squirrel.head())
    else:
        print("Failed to download CSV file")


    
'''
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # 寫入標題行
    writer.writerow(['開盤價','最高價','最低價', '收盤價','Adj Close','Volume'])
    # 寫入資料
    writer.writerows(data)
    
'''

