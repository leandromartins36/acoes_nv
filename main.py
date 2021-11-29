# %%
# import pandas_datareader.data as web
from bs4 import BeautifulSoup as bs
# import ssl
import pandas as pd
import requests as rs
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import time
import glob
import pyodbc
import os
# from tkinter import *
# import tkinter.filedialog
# from tkinter import messagebox


# %%

# navegador = webdriver.Firefox(executable_path='./geckodriver.exe')
# navegador.set_preference("browser.privatebrowsing.autostart", True)
# firefox_options = Options()
# firefox_options.add_argument("--headless")
# navegador.maximize_window()
# agente = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
# headers = {'User-Agent': agente}


# %%

chrome_options = Options()
chrome_options.add_argument("--headless")
navegador = webdriver.Chrome(chrome_options=chrome_options)
navegador.maximize_window()
agente = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
headers = {'User-Agent': agente}


# %%
# percorre a requisição e captura o html de cada pagina
# dataframe vindo da planilha de empresas.
empresas_df = pd.read_excel('EmpresasInfomoney.xlsx')
url = "https://www.infomoney.com.br/cotacoes/"
tabelaResul = []
contador = 0
while (contador < len(empresas_df)):
    for empresa in empresas_df["Empresas"]:
        url_nv = ''.join([url, empresa, '/historico/'])
        # print(empresa)
        navegador.get(url_nv)
        time.sleep(5)
        conteudo = rs.get(url_nv, headers=headers)
        time.sleep(3)
        # encontra o elemento da pagina e grava na memoria os dados da tabela.
        tb_din = navegador.find_element_by_xpath(
            '//*[@id="quotes_history"]').get_attribute('outerHTML')
        sigla_html = navegador.find_element_by_xpath(
            '/html/body/div[4]/div/div[1]/div[1]/div/div[1]/h1')
        # , index_col="DATA" incluir após thousands para colocar a data como indice.
        pd_html = pd.read_html(tb_din, decimal=',', thousands='.')
        df = pd.DataFrame(pd_html[0])
        df['EMPRESA'] = sigla_html.text
        time.sleep(3)
        tabelaResul.append(df.head(1))
        contador += 1
        time.sleep(3)


# %%
# 
url_cxco11 = "https://www.infomoney.com.br/cotacoes/fundos-imobiliarios-cxco11/"
Empresa_cx = ''
navegador.get(url_cxco11)

cx_fechamento = navegador.find_element_by_xpath(
    '/html/body/main/section/div/div/div[1]/div[2]/div[1]/span[1]').get_attribute('outerHTML')
cx_sigla_html = navegador.find_element_by_xpath(
    '/html/body/main/section/div/div/div[1]/div[1]/div/h1').get_attribute('outerHTML')
cx_fechamento_bs = bs(cx_fechamento, parser='html.parser')
cx_sigla = bs(cx_sigla_html, parser='html.parser')

cx_data_df = pd.DataFrame(tabelaResul[0])
cx_data_df['DATA']

cxco11_list1 = pd.Series(cx_data_df['DATA'])
cxco11_list2 = pd.Series(float(cx_fechamento_bs.text.replace(",", ".")), name='FECHAMENTO')
cxco11_list3 = pd.Series(cx_sigla.text, name='EMPRESA')

df_cxco11 = pd.concat([cxco11_list1, cxco11_list2, cxco11_list3], axis=1)

df_cxco11.to_excel(f'acoesfiltradas/cxco1.xlsx',
                   columns=['DATA', 'FECHAMENTO', 'EMPRESA'],  index=False)


# %%
def criar_plans_filtradas():
    acoes_tratadas = []
    for i in range(len(empresas_df)):
        pdf = pd.DataFrame(tabelaResul[i].head(2), columns=None)
        acoes_tratadas.append(pdf[['DATA', 'FECHAMENTO', 'EMPRESA']])
        acoesfiltradas = pdf.to_excel(f'acoesfiltradas/acoesfiltradas{i}.xlsx', columns=[
                                      'DATA', 'FECHAMENTO', 'EMPRESA'],  index=False)


# %%
dados_historicos = pd.DataFrame()


def juntar_planilhas():
    dados_historicos = pd.DataFrame()
    dados = glob.glob('acoesfiltradas\*.xlsx')
    dados_historicos += dados_historicos
    for i in dados:
        tabela = pd.read_excel(i)
        dados_historicos = pd.concat(
            [dados_historicos, tabela], axis=0, ignore_index=True)
    dados_historicos.to_excel('./acoesfiltradas.xlsx', index=False)


# %%
# prepara_sql = pd.read_excel('./acoesfiltradas.xlsx')

# %%
def SQLInserirDados(TabelaRecebeDados):
    prepara_sql = pd.read_excel('./acoesfiltradas.xlsx')
    dados_historicos = prepara_sql
    try:

        cnxn = pyodbc.connect('Trusted_Connection=yes',
                              driver='{SQL Server}',
                              server='LEANDROPC\SQLDEVELOPER2019',
                              database='ACOESINFO')

        cursor = cnxn.cursor()
        # Insert Dataframe into SQL Server:
        for index, row in dados_historicos.iterrows():
            cursor.execute("INSERT INTO [ACOESINFO].[dbo].[ACOESINFOMONEY] ( [DATA],[FECHAMENTO],[EMPRESA]) values(?,?,?)",
                           row.DATA, row.FECHAMENTO, row.EMPRESA)

        cnxn.commit()
        print("Inserindo dados")
    except ConnectionError as e:
        print("Erro de conexão: ", e)

    finally:

        cursor.close()
        cnxn.close()


# %%
def selectDatdos(consultar):

    try:
        connStr = pyodbc.connect('Trusted_Connection=yes',
                                 driver='{SQL Server}',
                                 server='LEANDROPC\SQLDEVELOPER2019',
                                 database='ACOESINFO')

        saida = pd.read_sql(consultar, connStr)
        return saida
        print("consultando")
    except ConnectionError as e:
        print("Erro de conexão: ", e)


# %%


criar_plans_filtradas()
time.sleep(0.1)
juntar_planilhas()
time.sleep(0.1)
navegador.quit()


# %%
SQLInserirDados('[ACOESINFO].[dbo].[ACOESINFOMONEY]')
time.sleep(0.1)
selectDatdos(consultar="select * FROM [ACOESINFO].[dbo].[ACOESINFOMONEY]")