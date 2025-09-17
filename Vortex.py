#BIBLIOTECAS
import time
import os
from flask_cors import CORS
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from flask import Flask, jsonify, render_template


#INICIO
api_key = os.environ.get('API_KEY', 'default-key')
app = Flask(__name__)
CORS(app)

#DEFs DE RASPAGEM

def close_indice():


#MEIO (PARTE 1)
@app.route('/')
def homepage():
    return render_template

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "API CLOSE",
        "endpoints": [
            "/close/value"
        ]
    }),



#MEIO (PARTE 2)
#AQUI EU COLOCO AS DEFs DE RETORNO


@app.route('/close/indice', methods=['GET'])
def api_close_indice():
    resultado = close_indice()
    return jsonify(resultado)

@app.route('/close/value', methods=['GET'])
def api_value():
    return jsonify({
        "Fechamento": close_indice()
    })

#FIM
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))