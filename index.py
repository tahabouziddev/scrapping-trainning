import requests
from bs4 import BeautifulSoup

URL = 'https://gogoanime.so/haikyuu-to-the-top-2nd-season-episode-11'
headers= {"user-agent":'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}


page= requests.get(URL,headers=headers)

soup= BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())
yes=soup.find('iframe')['src']
print(yes)