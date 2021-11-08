import pandas as pd
import requests as rs
# from IPython.display import HTML
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from urllib.error import URLError, HTTPError
import urllib
from urllib.request import urlopen, Request
import ssl
from selenium import webdriver
from selenium.webdriver import Firefox

navegador = webdriver.Firefox(executable_path='./geckodriver.exe')
navegador.maximize_window()

agente = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'

url = 'https://www.infomoney.com.br/cotacoes/fundo-imobiliario-cxco11/historico/'

headers = {'User-Agent': agente}
gcontext = ssl.SSLContext()

navegador.get(url)



#info = urllib.request.urlopen(url, context=gcontext).read()
info = rs.get(url, headers=headers)

html = bs(info.text, 'html.parser')

# data_acao, fechamento = [],[]
html = html.findAll('table', id = 'quotes_history')
''' data_acao.append(html[0].text)
fechamento.append(html[2].text) '''

df = pd.DataFrame(html)

print(df)