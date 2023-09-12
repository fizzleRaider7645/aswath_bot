import requests

def get_news(query):
    api_key = 'your-api-key'
    base_url = 'https://gnews.io/api/v4/search?'
    final_url = f"{base_url}q={query}&token={api_key}"
    response = requests.get(final_url)
    data = response.json()
    return data
