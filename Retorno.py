import httpx

# GET request simples
resp = httpx.get("https://www.youtube.com/")
print(resp.status_code)   # Código da resposta (200, 404, etc.)
print(resp.json())        # Converte o JSON da resposta


#headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'