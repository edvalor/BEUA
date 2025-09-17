from playwright.sync_api import sync_playwright
import time

robo = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'
url = 'https://indexes.nasdaqomx.com/Index/Overview/nbi'

with sync_playwright() as pw:
    site = pw.chromium.launch(headless=False) # Qual navegador deve abrir
    contexto = site.new_context(user_agent=robo) # Simula um user_agent
    pagina = contexto.new_page() # Abre uma aba (pagina)
    pagina.goto(url) # Link do site
    pagina.wait_for_selector('//*[@id="hero"]/article/div/div[1]/div[2]/data[1]') # Espera o elemento aparecer
    valor = pagina.inner_text('//*[@id="hero"]/article/div/div[1]/div[2]/data[1]') # Busca por ele
    print(valor) # Retorno
    

    time.sleep(5)
    site.close()