# BIBLIOTECAS
import os
from datetime import date
import json
from flask_cors import CORS
from playwright.sync_api import sync_playwright
from flask import Flask, jsonify

# FUNÇÃO PRINCIPAL DE RASPAGEM


def coletar_todos(indices, nome_saida):
    resultados = {}
    robo = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'
    
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)  # True= sem tela, False= com tela
        context = browser.new_context(user_agent=robo)
        page = context.new_page()

        for nome, config in indices.items():
            try:
                print(f"Coletando {nome}")
                page.goto(config["url"], timeout=60000)
                page.wait_for_selector(config["selector"], timeout=30000)
                resultados[nome] = page.inner_text(config["selector"])
            except Exception as e:
                resultados[nome] = f"Erro: {str(e)}"

        browser.close()

    with open(nome_saida, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
        


    print(f"Arquivo {nome_saida}!")
    return resultados

data_hoje = date.today()
data_ptBR = data_hoje.strftime("%d/%m/%Y")


indices = {
    "TA125": {
        "url": "https://www.tase.co.il/en/market_data/index/137/major_data",
        "selector": 'div.bond_rate_num',
    },
    "SMI": {
        "url": "https://www.six-group.com/en/products-services/the-swiss-stock-exchange/market-data/indices/equity-indices/smi.html",
        "selector": 'div._closingPrice_de68u_13',
    },
    "N100": {
        "url": "https://live.euronext.com/en/product/indices/fr0003502079-xpar/euronext-100/n100",
        "selector": 'span.display-5',
        
    },
    "N150": {
        "url": "https://live.euronext.com/en/product/indices/FR0003502087-XPAR",
        "selector": 'span.display-5',
        
    },
    "PSI20": {
        "url": "https://live.euronext.com/en/product/indices/pting0200002-xlis/psi-20/psi20",
        "selector": 'span.display-5',
        
    },
    "BEL20": {
        "url": "https://live.euronext.com/en/product/indices/be0389555039-xbru/bel-20/bel20",
        "selector": 'span.display-5',
        
    },
    "ASCX": {
        "url": "https://live.euronext.com/en/product/indices/nl0000249142-xams/ascx-index/ascx",
        "selector": 'span.display-5',
        
    },
    "CAC40": {
        "url": "https://live.euronext.com/en/product/indices/fr0003500008-xpar/cac-40/px1",
        "selector": 'span.display-5',
        
    },
    "EUROTOP100": {
        "url": "https://live.euronext.com/en/product/indices/NL0000245710-XAMS",
        "selector": 'span.display-5',
        
    },
    "FTSE100": {
        "url": "https://www.londonstockexchange.com/indices?tab=ftse-indices",
        "selector": 'td.hide-on-portrait',
        
    },
    "NMX": {
        "url": "https://www.londonstockexchange.com/indices/ftse-350",
        "selector": 'span.price-tag',
        
    },
    "MCX": {
        "url": "https://www.londonstockexchange.com/indices/ftse-250",
        "selector": 'span.price-tag',
        
    },
    "JALSH": {
        "url": "https://br.tradingview.com/symbols/NSE-JASH/",
        "selector": 'span.last-zoF9r75I.js-symbol-last',
        
    },
    "KOSPI": {
        "url": "https://global.krx.co.kr/main/main.jsp",
        "selector": '//*[@id="section1"]/div/div/div[3]/ul/li[2]/span[2]',
        
    },
    "WIG": {
        "url": "https://www.gpw.pl/en-home",
        "selector": '//*[@id="chart-PL9999999987"]/div[1]/span[1]',
        
    },
    "XAO": {
        "url": "https://www2.asx.com.au/markets/company/xao",
        "selector": '//*[@id="realTimeIndicesWidgetData"]/tr[9]/td[6]',
        
    },
    "NIKKEI": {
        "url": "https://www.tradingview.com/symbols/FRED-NIKKEI225/",
        "selector": 'span.last-zoF9r75I.js-symbol-last',
        
    },
    "SSE": {
        "url": "https://br.tradingview.com/symbols/SSE-000001/",
        "selector": 'span.last-zoF9r75I.js-symbol-last',
        
    },
    "OMXC20": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/OMXC20",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "IXCO": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/Ixco",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "IXTC": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/ixtc",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "NBI": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/nbi",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "BANK": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/bank",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "INDS": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/Inds",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "INSR": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/Insr",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "NQBTC": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/NQBTC",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "NQETH": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/NQETH",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]',
        
    },
    "GD": {
        "url": "https://www.athexgroup.gr/en",
        "selector": 'div.ticker-tape-value.textColorGrey7',
        
    },
    "IBC": {
        "url": "https://www.bolsadecaracas.com/",
        "selector": 'h2.mb-0.pl-2.font-weight-normal',
        
    },
    "NCI":  {
        "url": "https://www.nasdaq.com/market-activity/index/nci#google_vignette",
        "selector": 'div.nsdq-quote-header__pricing-information-saleprice'
    },
    "SPTSX": {
        "url": "https://www.spglobal.com/spdji/en/indices/equity/sp-tsx-composite-index/#overview",
        "selector": 'div.index-level '
    },
    "SP100": {
        "url": "https://www.spglobal.com/spdji/en/indices/equity/sp-100/#overview",
        "selector": 'div.index-level'
    },
    "OMXS30": {
        "url": "https://www.nasdaq.com/european-market-activity/indexes/omxs30?id=SE0000337842",
        "selector": 'div.nsdq-quote-header__pricing-information-saleprice'
    },
    "HSI": {
        "url": "https://www.tradingview.com/symbols/HSI-HSI/",
        "selector": 'span.last-zoF9r75I.js-symbol-last'
    },
    "TAIEX": {
        "url": "https://www.tradingview.com/symbols/OSE-TAIEX1!/",
        "selector": 'span.last-zoF9r75I.js-symbol-last'
    },
    "IPSA": {
        "url": "https://www.tradingview.com/symbols/BCS-SP_IPSA/",
        "selector": 'span.last-zoF9r75I.js-symbol-last'
    },
    "FTSEMIB": {
        "url": "https://www.tradingview.com/symbols/FTSE-FTSEMIB/",
        "selector": 'span.last-zoF9r75I.js-symbol-last'
    },

    "SZSE": {
        "url": "http://www.szse.cn/English/index.html",
        "selector": 'div.title.up',
        
    },
    "SPTSX": {
        "url": "https://www.spglobal.com/spdji/en/indices/equity/sp-tsx-composite-index/#overview",
        "selector": 'div.index-level',
        
    },
    "IPC": {
        "url": "https://www.bmv.com.mx/",
        "selector": '//*[@id="viewIPC"]/dd/ul/li[1]/span',
        
    },
    "ETHUSD_RR": {
        "url": "https://www.cmegroup.com/markets/cryptocurrencies/cme-cf-cryptocurrency-benchmarks.html",
        "selector": '//*[@id="main-content"]/div/div[4]/div/div[3]/div[2]/div/div/div/section[1]/div[1]/div/span',
        
    },
    "ETHUSD_RTI": {
        "url": "https://www.cmegroup.com/markets/cryptocurrencies/cme-cf-cryptocurrency-benchmarks.html",
        "selector": '//*[@id="main-content"]/div/div[4]/div/div[3]/div[2]/div/div/div/section[1]/div[2]/div/span',
        
    },
    "MERVAL": {
        "url": "https://open.bymadata.com.ar/#/technical-detail-ei-index?symbol=M",
        "selector": '//*[@id="mat-tab-content-0-0"]/div/mdp-historical-serie-ei-index-tab/div[2]/div/div[2]/mdp-normalizer-table/div/div/div/table/tbody/tr[11]/td[6]/span',       
    },
    "DAX": {
        "url": "https://www.tradingview.com/symbols/XETR-DAX/",
        "selector": 'span.last-zoF9r75I.js-symbol-last',       
    },
    "SP500": {
        "url": "https://www.spglobal.com/spdji/en/indices/equity/sp-500/#overview",
        "selector": 'div.index-level',       
    },
    "AMX": {
        "url": "https://www.tradingview.com/symbols/EURONEXT-AMX/",
        "selector": 'span.last-zoF9r75I.js-symbol-last',       
    },
    "DJI": {
        "url": "https://www.spglobal.com/spdji/en/indices/equity/dow-jones-industrial-average/#overview",
        "selector": 'div.index-level'
    },
    "NASDAQ": {
        "url": "https://www.nasdaq.com/market-activity/index/comp",
        "selector": 'div.nsdq-quote-header__pricing-information-saleprice'
    },
    "NASDAQ100": {
        "url": "https://www.nasdaq.com/market-activity/index/ndx",
        "selector": 'div.nsdq-quote-header__pricing-information-saleprice'
    },
    
}


if __name__ == "__main__":
    while True:
            print("Carregando...")
            coletar_todos(indices, "dados.json")

            resposta = input("Quer atualizar os valores? (Y/N): ").strip().lower()
            if resposta != "y":
                print("Saindo...")
                break
