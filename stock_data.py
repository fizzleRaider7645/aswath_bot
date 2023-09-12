import requests

def get_stock_price(symbol):
    api_key = 'your-api-key'
    base_url = 'https://www.alphavantage.co/query?'
    function = 'TIME_SERIES_DAILY'
    datatype = 'json'
    final_url = f"{base_url}function={function}&symbol={symbol}&apikey={api_key}&datatype={datatype}"
    response = requests.get(final_url)
    data = response.json()
    return data
