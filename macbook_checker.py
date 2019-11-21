import requests
from bs4 import BeautifulSoup
import time

def get_price():
    URLA = 'https://www.amazon.com/Apple-MacBook-Retina-Display-1-6GHz/dp/B07PND7BPZ/ref=pd_sbs_147_2/130-6809817-8958661?_encoding=UTF8&pd_rd_i=B07PND7BPZ&pd_rd_r=58679cc4-8cb1-48dd-87a1-51684a258fee&pd_rd_w=zS5bS&pd_rd_wg=uWAtL&pf_rd_p=43281256-7633-49c8-b909-7ffd7d8cb21e&pf_rd_r=9WWME0H5V99409Y1NYRC&psc=1&refRID=9WWME0H5V99409Y1NYRC'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    page = requests.get(URLA, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    price = soup2.find(id = 'priceblock_ourprice').get_text().replace(',','')


    currentprice = float(price[1:])

    if currentprice > 1000:
        print("Price has raised to ", currentprice)
    else:
        print(currentprice)




while(True):
    print('\n')
    print('Current Price')
    print('\n')
    get_price()
    print('\n')
    time.sleep(15)