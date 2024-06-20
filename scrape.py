import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_stock_data(tickers, pages = 1):
    stocks = []

    for ticker in tickers:
        for page in range(1, pages+1):
            url = f'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}&offset={page * 100}&count=100'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            for row in soup.find_all('tr', class_='BdT'):
                cols = row.find_all('td')
                if len(cols) < 7:
                    continue
                date = cols[1].text
                
