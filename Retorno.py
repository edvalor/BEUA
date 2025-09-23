# BIBLIOTECAS
import os
from flask_cors import CORS
from playwright.sync_api import sync_playwright
from flask import Flask, jsonify

# INICIO
api_key = os.environ.get('API_KEY', 'default-key')
app = Flask(__name__)
CORS(app)

# FUNÇÃO PRINCIPAL DE RASPAGEM
def playw(url: str, selector: str):
    ChatBot = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(user_agent=ChatBot)
        page = context.new_page()
        page.goto(url, timeout=60000)

        page.wait_for_selector(selector, timeout=30000)
        close = page.inner_text(selector)  # pega o texto do índice

        page.close()
        browser.close()

        return close

# FUNÇÃO ESPECÍFICA PARA DJI
def indice():
    url = "https://www.spglobal.com/spdji/en/indices/equity/dow-jones-industrial-average/#overview"
    selector = "div.index-level"   # Ajustar se o seletor mudar
    value = playw(url, selector)

    return {
        "Indice": "DJI",
        "Valor": value,
        "Moeda": "USD"
    }

# ROTAS FLASK
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "API CLOSE",
        "endpoints": [
            "/close/indice"
        ]
    })

@app.route('/close/indice', methods=['GET'])
def api_close_indice():
    resultado = indice()
    return jsonify(resultado)

# FIM
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
