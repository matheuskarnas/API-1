import os
from dotenv import load_dotenv
import mysql.connector
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Carregando as variáveis de ambiente
load_dotenv()

class Config:
    DBUSER = os.getenv('DBUSER')
    DBPASS = os.getenv('DBPASS')
    DBHOST = os.getenv('DBHOST')
    DBNAME = os.getenv('DBNAME')

# Dicionário de configuração do banco de dados
datacfg = {
    'user': Config.DBUSER,
    'password': Config.DBPASS,
    'host': Config.DBHOST,
    'database': Config.DBNAME  
}

# Tentativa de conexão com o banco de dados
try:
    connection = mysql.connector.connect(
        user=datacfg['user'],
        password=datacfg['password'],
        host=datacfg['host'],
        database=datacfg['database']
    )

    if connection.is_connected():
        print("Conectado ao banco de dados")
    else:
        print("Falha na conexão com o banco de dados")

    cursor = connection.cursor()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    urls_vereadores = [
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
    ]

    for url in urls_vereadores:
        driver.get(url)
        time.sleep(3)

        try:
            print("Tentando capturar as informações...")
            foto_vereador = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_foto_parlamentar img")
            nome_vereador = driver.find_element(By.ID, "nome_parlamentar")
            partido_vereador = driver.find_element(By.ID, "partido")
            informacoes = driver.find_element(By.ID, "dados_parlamentar")

            nome_vereador = nome_vereador.text
            img_src = foto_vereador.get_attribute("src")
            partido_vereador = partido_vereador.text
            informacoes = informacoes.text

            if nome_vereador and img_src:
                print(f"Escrevendo o nome do {nome_vereador}...")
                with open("informacoes_vereadores.txt", "a", encoding="utf-8") as file:
                    file.write(f"Nome: {nome_vereador}\n")
                    file.write(f"Url_Imagem: {img_src}\n")
                    file.write(f"Partido: {partido_vereador}\n")
                    file.write(f"Informações: {informacoes}\n")
                    file.write("-" * 40 + "\n")

            # Quebrar os dados em outras variáveis
            infos_quebradas = {}
            for line in informacoes.splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    infos_quebradas[key.strip()] = value.strip()

            # Acessando as informações
            telefone = infos_quebradas.get("Telefone(s)", None)
            celular = infos_quebradas.get("Celular", None)
            email = infos_quebradas.get("E-mail", None)
            gabinete = infos_quebradas.get("Nº do Gabinete", None)

            # Inserindo dados no banco de dados
            try:
                sql = """INSERT INTO tb_vereador (vere_nome, vere_partido, vere_telefone, vere_email, vere_img_url) VALUES (%s, %s, %s, %s, %s)"""
                values = (nome_vereador, partido_vereador, telefone, email, img_src)
                cursor.execute(sql, values)
                connection.commit()
                print(f"Dados de {nome_vereador} inseridos com sucesso!")
            except mysql.connector.Error as err:
                print(f"Erro ao inserir dados: {err}")

        except Exception as e:
            print(f"Erro ao capturar dados da página {url}: {e}")

except mysql.connector.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
    driver.quit()
