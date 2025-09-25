import json
from playwright.sync_api import sync_playwright

# Função genérica Playwright
def playw(url: str, selector: str):
    robo = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(user_agent=robo)
        page = context.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_selector(selector, timeout=30000)
        value = page.inner_text(selector)
        browser.close()
        return value

# Índices que você quer
indices = {
    "DJI": {
        "url": "https://www.spglobal.com/spdji/en/indices/equity/dow-jones-industrial-average/#overview",
        "selector": "div.index-level" 
    },
    "NBI": {
        "url": "https://indexes.nasdaqomx.com/Index/Overview/nbi",
        "selector": '//*[@id="hero"]/article/div/div[1]/div[2]/data[1]'
    },
    # Adicione aqui os outros índices no mesmo formato
}

# Rodar e salvar
print('Carregando...')
resultados = {}
for nome, config in indices.items():
    try:
        resultados[nome] = playw(config["url"], config["selector"])
    except Exception as e:
        resultados[nome] = f"Erro: {str(e)}"

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

print("✅ Arquivo dados.json gerado com sucesso!")
