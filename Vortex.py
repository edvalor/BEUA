#BIBLIOTECAS
import os
import time
from flask_cors import CORS
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from flask import Flask, jsonify, render_template


#INICIO
api_key = os.environ.get('API_KEY', 'default-key')
app = Flask(__name__)
CORS(app)

#DEFs DE RASPAGEM

def playw(url: str, selector: str):
    ChatBot = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'
    results = {}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(user_agent=ChatBot)
        page = context.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_selector(selector, timeout=30000)
        close = page.inner_text(selector)
        page.close()
        browser.close()
        return close

# Américas
def DJI():
    # Estados Unidos - América do Norte
    url = 'https://www.spglobal.com/spdji/en/indices/equity/dow-jones-industrial-average/#overview'
    selector = "div.index-level"
    value = playw(url, selector)

    return {
        "Indice": "DIJ",
        "DIJ": value,
        "Contry": "USD"
    }

    pass

def DJU():
    # Estados Unidos - América do Norte
    pass

def SP100():
    # Estados Unidos - América do Norte
    pass

def SP500():
    # Estados Unidos - América do Norte
    pass

def NASDAQ():
    # Estados Unidos - América do Norte
    pass

def NASDAQ100():
    # Estados Unidos - América do Norte
    pass

def NBI():
    # Estados Unidos - América do Norte
    pass

def BANK():
    # Estados Unidos - América do Norte
    pass

def INDS():
    # Estados Unidos - América do Norte
    pass

def INSR():
    # Estados Unidos - América do Norte
    pass

def NQBTC():
    # Estados Unidos - América do Norte
    pass

def NQETH():
    # Estados Unidos - América do Norte
    pass

def NCI():
    # Estados Unidos - América do Norte
    pass

def SPTSX():
    # Canadá - América do Norte
    pass

def IPC():
    # México - América do Norte
    pass

def IXCO():
    # México - América do Norte
    pass

def IXTC():
    # México - América do Norte
    pass

def MERVAL():
    # Argentina - América do Sul
    pass


# Europa
def FTSE100():
    # Reino Unido - Europa
    pass

def NMX():
    # Reino Unido - Europa
    pass

def DAX():
    # Alemanha - Europa
    pass

def CAC40():
    # França - Europa
    pass

def FTSEMIB():
    # Itália - Europa
    pass

def IBC():
    # Espanha - Europa
    pass

def PSI20():
    # Portugal - Europa
    pass

def SMI():
    # Suíça - Europa
    pass

def BEL20():
    # Bélgica - Europa
    pass

def AMX():
    # Holanda - Europa
    pass

def ASCX():
    # Holanda - Europa
    pass

def AEX():
    # Holanda - Europa
    pass

def OMXC20():
    # Dinamarca - Europa
    pass

def OMXS30():
    # Suécia - Europa
    pass

def WIG():
    # Polônia - Europa
    pass

def GD():
    # Grécia - Europa
    pass

def EUROTOP100():
    # Zona Euro - Europa
    pass

def N100():
    # Zona Euro - Europa
    pass

def N150():
    # Zona Euro - Europa
    pass

def MCX():
    # Russia - Europa
    pass

# Ásia e Oceania
def NIKKEI():
    # Japão - Ásia
    pass

def SSE():
    # China - Ásia
    pass

def SZSE():
    # China - Ásia
    pass

def KOSPI():
    # Coreia do Sul - Ásia
    pass

def TA125():
    # Israel - Ásia
    pass

def XAO():
    # Austrália - Oceania
    pass

def JALSH():
    # África do Sul - África
    pass

# Criptomoedas
def ETHUSD_RR():
    # Global - Criptomoeda
    pass

def ETHUSD_RTI():
    # Global - Criptomoeda
    pass


#DJT
#IPSA


#MEIO (PARTE 1)
@app.route('/')
def homepage():
    return render_template

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "API CLOSE",
        "endpoints": [
            "/close/DJI",
            "/close/DJU",
            "/close/SP100",
            "/close/SP500",
            "/close/NASDAQ",
            "/close/NASDAQ100",
            "/close/NBI",
            "/close/BANK",
            "/close/INDS",
            "/close/INSR",
            "/close/NQBTC",
            "/close/NQETH",
            "/close/NCI",
            "/close/SPTSX",
            "/close/IPC",
            "/close/IXCO",
            "/close/IXTC",
            "/close/MERVAL",
            "/close/FTSE100",
            "/close/NMX",
            "/close/DAX",
            "/close/CAC40",
            "/close/FTSEMIB",
            "/close/IBC",
            "/close/PSI20",
            "/close/SMI",
            "/close/BEL20",
            "/close/AMX",
            "/close/ASCX",
            "/close/AEX",
            "/close/OMXC20",
            "/close/OMXS30",
            "/close/WIG",
            "/close/GD",
            "/close/EUROTOP100",
            "/close/N100",
            "/close/N150",
            "/close/MCX",
            "/close/NIKKEI",
            "/close/SSE",
            "/close/SZSE",
            "/close/KOSPI",
            "/close/TA125",
            "/close/XAO",
            "/close/JALSH",
            "/close/ETHUSD_RR",
            "/close/ETHUSD_RTI",
        ]
    }),



#MEIO (PARTE 2)
#AQUI EU COLOCO AS DEFs DE RETORNO


@app.route('/close/DJI', methods=['GET'])
def api_close_DJI():
    resultado = DJI()
    return jsonify(resultado)

@app.route('/close/USD', methods=['GET'])
def api_close_USD():
    return jsonify({
        "DJI": DJI(),
    })


@app.route('/close/value', methods=['GET'])
def api_value():
    return jsonify({
        "Fechamento": DJI()
    })

#FIM
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
