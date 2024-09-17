# Para rodar o script instalar as bibliotecas selenium e webdriver:
# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import requests

os.makedirs("fotos_vereadores", exist_ok=True)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
urls_vereadores = (
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=245',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=43',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=249',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=44',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=35',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=240',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=242',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=238',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=50',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=38',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=55',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=239',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=246',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=247',
    # 'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=257',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=237',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=243',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=45',
    'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=40',
    # 'https://camarasempapel.camarasjc.sp.gov.br/spl/comissao.aspx?id=41',
    # 'https://camarasempapel.camarasjc.sp.gov.br/spl/comissao.aspx?id=42',
)
vereadores_encontrados_nome = []
vereadores_encontrados_img = []

try:
    for urls in urls_vereadores:
        driver.get(urls)
        time.sleep(3)

        try:
            print("Tentando Capturar as informações...")
            foto_vereador = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_foto_parlamentar img")
            nome_vereador = driver.find_element(By.ID, "nome_parlamentar")
            partido_vereador = driver.find_element(By.ID, "partido")
            
            nome_vereador = nome_vereador.text
            img_src = foto_vereador.get_attribute("src")
            partido_vereador = partido_vereador.text

            if nome_vereador and img_src:
                print(f"Escrevendo o nome do {nome_vereador}...")
                with open("informacoes_vereadores.txt", "a", encoding="utf-8") as file:
                    file.write(f"Nome: {nome_vereador}\n")
                    file.write(f"Url_Imagem: {img_src}\n")
                    file.write(f"Partido: {partido_vereador}\n")
                    file.write("-"*40 + "\n")

                vereadores_encontrados_nome.append(nome_vereador)

                try:
                    print(f"Baixando imagem do {nome_vereador}...")
                    img_data = requests.get(img_src).content
                    filename = f"fotos_vereadores/{nome_vereador}.jpg"
                    with open(filename, "wb") as img_file:
                        img_file.write(img_data)
                    vereadores_encontrados_img.append(nome_vereador)


                except Exception as e:
                    print(f"Erro ao baixar a imagem: {e}")
            else:
                print("Não foi possível encontrar o nome ou a imagem do vereador.")

        except Exception as e:
            print(f"Erro ao capturar dados da página {urls}: {e}")
except Exception as e:
    print(f"Algo deu muito errado: {e}")


finally:


    driver.quit()
    os.system("clear") 
    print("Programa finalizado")
    res = input("Deseja ver os resultados no terminal? [S]im ou [N]ão")
    if res.upper().startswith("S"):
        print("-"*60)
        print("IMGS:")
        print(vereadores_encontrados_img)
        print("\n")
        print("-"*60)
        print("NOMES:")
        print(vereadores_encontrados_nome)
        print("-"*60)
    else:
        os.system("clear")
        print("Saindo...")

