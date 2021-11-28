# gcontext = ssl.SSLContext() usado junto com a biblioteca urllib
# url = "https://www.infomoney.com.br/cotacoes/"
# navegador.get(url)
# navegador.find_element_by_xpath('/html/body/div[7]/div/div[1]/div[2]/div/table/thead/tr/th[1]').click() #faz a ordenação da coluna de data no site do infomoney
# display(pd_html[0].head())
# pd_html[0].info()
# pd_html[0]
# df.info()
# df.astype('str').dtypes
# df[['FECHAMENTO']].head(1)
#navegador = webdriver.Firefox(executable_path='./geckodriver.exe', options=firefox_options)
# navegador.maximize_window()
#sigla_re = re.findall(r'\((.*?)\)',sigla_html.text)
#sigla_series = pd.Series([sigla_re])
#sigla_df = pd.DataFrame([sigla_re])
# sigla_html = navegador.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div/div[1]/h1')
# sigla_re = re.findall(r'\((.*?)\)',sigla_html.text)
# sigla_str = sigla_html.text[-7:-1]
# sigla_str
# sigla_str = sigla_html.text[sigla_re]
#sigla_series = pd.DataFrame(sigla_re)
# sigla_series
#sigla_str = sigla_html.text[-7:-1]
#sigla_str = re.findall(r'\((.*?)\)',sigla_html.text)
# ##### bibliotecas utilizadas na captura dos dados.
# from urllib.error import URLError, HTTPError
# import urllib
# # import re #regex
# import numpy as np
# from urllib.request import urlopen, Request
# import pandas as pd
# import requests as rs
# import numpy as np
# from urllib.request import urlopen, Request
# from bs4 import BeautifulSoup as bs
# from urllib.error import URLError, HTTPError
# import urllib
# from urllib.request import urlopen, Request
# import ssl
# from selenium import webdriver
# from selenium.webdriver import Firefox
# import time

# navegador = webdriver.Firefox(executable_path='./geckodriver.exe')
# navegador.maximize_window()
# agente = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'

# # url = 'https://www.infomoney.com.br/cotacoes/fundo-imobiliario-cxco11/historico/'

# headers = {'User-Agent': agente}
# #gcontext = ssl.SSLContext()

# empresas_df = pd.read_excel('EmpresasInfomoney.xlsx')
# url = "https://www.infomoney.com.br/cotacoes/"

# contador = 0
# while (contador < len(empresas_df)):
#     for empresa in empresas_df["Empresas"]:
#         url_nv = ''.join([url,empresa,'/historico/'])
#         #print(empresa)
#         navegador.get(url_nv)
#         time.sleep(5)
#         conteudo = rs.get(url_nv, headers=headers)
#         time.sleep(2)
#         tb_din = navegador.find_element_by_xpath('//*[@id="quotes_history"]').get_attribute('outerHTML')#encontra o elemento da pagina e grava na memoria os dados da tabela.
#         pd_html = pd.read_html(tb_din, decimal = ',', thousands = '.', index_col="DATA") 
#         time.sleep(2)
#         contador +=1  
#         time.sleep(3)  
#         print(pd_html[0].head())

import sys
import platform
import imp

print("Python EXE     : " + sys.executable)
print("Architecture   : " + platform.architecture()[0])


raw_input("\n\nPress ENTER to quit")