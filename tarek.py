import requests
from bs4 import BeautifulSoup

print('coin name   /', 'short cut  /', 'coin price   /', 'rate of change   /', '24h_volume')
# How much cryptocurrency has been traded over a set period, such as the past 24 hours.


r = requests.get("https://crypto.com/price?page=1")

soup = BeautifulSoup(r.content, "lxml")

name = soup.find_all('p', {'class': 'chakra-text css-rkws3'})

short_cut = soup.find_all('span', {'class': 'chakra-text css-1jj7b1a'})

price = soup.find_all('div', {'class': 'css-0'})

rate_of_change = soup.find_all('p', {'class': 'chakra-text css-z6ljr8'})
#
rate_of_change1 = soup.find_all('p', {'class': 'chakra-text css-1okxd'})
rate = [*rate_of_change1, *rate_of_change]

_24h_vol = soup.find_all('td', {'class': 'css-1nh9lk8'})

for i in range(len(name)):
    print(name[i].text, '   /', short_cut[i].text, '    /', price[i].text, '    /', rate[i].text, ' /', _24h_vol[i].text)