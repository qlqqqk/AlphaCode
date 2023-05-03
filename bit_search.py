import requests
import pandas as pd
from time import gmtime,localtime

def current_price(coin): #자산별 현재가 정보

    url = f"https://api.bithumb.com/public/ticker/{coin}_KRW"

    headers = {
        "accept": "application/json"
        
            }

    response = requests.get(url, headers=headers)
    print(response.text)
    
    
def price_df():
    #ALL 현재가 정보
    url = "https://api.bithumb.com/public/ticker/ALL_KRW"

    headers = {
        "accept": "application/json"
        
            }

    response = requests.get(url, headers=headers)

    
    info = response.json()
    dictdf = pd.DataFrame.from_dict(info).drop('date').drop('status',axis=1)
    df = pd.json_normalize(dictdf['data'])
    df['coin_name'] = dictdf.index
    df = df[df.columns[-1:].to_list() + df.columns[:-1].to_list()]
    
    utc = gmtime(int(info['data']['date'])/1000) # 국제표준시 기준
    
    return df,utc