import pandas as pd
import requests as rs
import numpy as np
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from urllib.error import URLError, HTTPError
import urllib
from urllib.request import urlopen, Request
import ssl
from selenium import webdriver
from selenium.webdriver import Firefox
import time

navegador = webdriver.Firefox(executable_path='./geckodriver.exe')
navegador.maximize_window()
agente = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'

# url = 'https://www.infomoney.com.br/cotacoes/fundo-imobiliario-cxco11/historico/'

headers = {'User-Agent': agente}
#gcontext = ssl.SSLContext()

empresas_df = pd.read_excel('EmpresasInfomoney.xlsx')
url = "https://www.infomoney.com.br/cotacoes/"

contador = 0
while (contador < len(empresas_df)):
    for empresa in empresas_df["Empresas"]:
        url_nv = ''.join([url,empresa,'/historico/'])
        #print(empresa)
        navegador.get(url_nv)
        time.sleep(5)
        conteudo = rs.get(url_nv, headers=headers)
        time.sleep(2)
        tb_din = navegador.find_element_by_xpath('//*[@id="quotes_history"]').get_attribute('outerHTML')#encontra o elemento da pagina e grava na memoria os dados da tabela.
        pd_html = pd.read_html(tb_din, decimal = ',', thousands = '.', index_col="DATA") 
        time.sleep(2)
        contador +=1  
        time.sleep(3)  
        print(pd_html[0].head())