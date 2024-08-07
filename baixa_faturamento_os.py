import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Tokens_IXC import *

# ----------- Options chrome -----------
options = Options()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# ----------- Configura Webdriver -----------
driver = webdriver.Chrome(options=options, service=Service(caminho_webdriver))


# ----------- find element by id -----------
def click_byid(id):
    driver.find_element(by=By.ID, value=id).click()


def send_byid(id, txt):
    driver.find_element(by=By.ID, value=id).send_keys(txt)


def clear_byid(id):
    driver.find_element(by=By.ID, value=id).clear()


def get_info_byid(id):
    driver.find_element(by=By.ID, value=id).get_attribute("innerHTML")


# ----------- find element by name -----------
def click_byname(name):
    driver.find_element(by=By.NAME, value=name).click()


def send_byname(name, txt):
    driver.find_element(by=By.NAME, value=name).send_keys(txt)


def clear_byname(name):
    driver.find_element(by=By.NAME, value=name).clear()


def get_info_byname(name):
    driver.find_element(by=By.NAME, value=name).get_attribute("innerHTML")


# ----------- find element by xpath -----------
def click_byxpath(x):
    driver.find_element(by=By.XPATH, value=x).click()


def send_byxpath(x, txt):
    driver.find_element(by=By.XPATH, value=x).send_keys(txt)


def clear_byxpath(x):
    driver.find_element(by=By.XPATH, value=x).clear()


def get_info_byxpath(x):
    driver.find_element(by=By.XPATH, value=x).get_attribute("innerHTML")


# ----------- find element by class -----------
def click_byclass(x):
    driver.find_element(by=By.CLASS_NAME, value=x).click()


def send_byclass(x, txt):
    driver.find_element(by=By.CLASS_NAME, value=x).send_keys(txt)


def clear_byclass(x):
    driver.find_element(by=By.CLASS_NAME, value=x).clear()


def get_info_byclass(x):
    driver.find_element(by=By.CLASS_NAME, value=x).get_attribute("innerHTML")


def login_ixc():
    # Realiza login no sistema IXC
    link = url_sistema
    driver.get(link)
    driver.maximize_window()

    send_byid('email', email)  # insere email
    send_byid('senha', senha)  # insere senha
    click_byid('entrar')  # clica em entrar
    time.sleep(1)
    try:
        click_byid('entrar')  # clica em entrar
        driver.implicitly_wait(10)  # seconds
        try:
            click_byxpath('//*[@id="warning"]/vg-body/div/vg-button[2]')  # fecha pop-up
        except:
            time.sleep(0.5)
    except:
        try:
            driver.implicitly_wait(10)  # seconds
            click_byxpath('//*[@id="warning"]/vg-body/div/vg-button[2]')  # fecha pop-up
        except:
            time.sleep(1)
            print('Erro login')
            driver.quit()


def acesso_faturamento_OS():
    # Acessa o campo de faturamento de OS
    driver.implicitly_wait(10)  # seconds
    click_byid('id_input_menu')  # abre pesquisa
    send_byid('id_input_menu', 'pedido')  # insere pesquisa
    click_byxpath(
        '//*[@id="grupo_menu07deb040a8a504d5c262c87677a5bf95"]/ul/li[2]/ul/li[3]')  # acessa menu pedido de ordem de serviço
    click_byxpath('//*[@id="1_grid"]/div/div[3]/div/span[2]/i')  # abre menu da grid
    click_byxpath('/html/body/div[2]/div/div[3]/nav[2]/ul/li')  # insere filtro salvo
    click_byxpath('//*[@id="1_grid"]/div/div[5]/div/table/thead/tr/th[2]')  # ordena para crescente
    click_byxpath('//*[@id="1_grid"]/div/div[5]/div/table/thead/tr/th[2]')  # ordena para decrescente
    time.sleep(3)


def baixa_faturamento_ativacao():
    # Realiza o faturamento da OS
    click_byname('btn_finalizar_pedido')  # finalizar pedido
    time.sleep(2)

    driver.implicitly_wait(10)  # seconds
    click_byid('previsaoN')  # insere previsão "não"
    time.sleep(0.1)

    driver.implicitly_wait(10)  # seconds
    click_byclass('disab')  # save
    time.sleep(0.5)

    driver.implicitly_wait(10)  # seconds
    click_byid('finalizar_saida')  # finalizar saida
    time.sleep(1)

    driver.implicitly_wait(10)  # seconds
    send_byid('id_carteira_cobranca', '2')  # inserir carteira de cobrança

    driver.implicitly_wait(10)  # seconds
    send_byid('id_carteira_cobranca', Keys.TAB)  # TAB no campo
    time.sleep(1)

    driver.implicitly_wait(10)  # seconds
    click_byxpath('/html/body/form[3]/div[2]/button[1]')  # salvar e gerar financeiro

    driver.implicitly_wait(10)  # seconds
    click_byid('validar_finalizar')  # validar e finalizar
    time.sleep(1)

    driver.implicitly_wait(10)  # seconds
    click_byid('vd_saida_fechamento_btn_close')  # fechar aba
    time.sleep(1)

    driver.implicitly_wait(10)  # seconds
    click_byid('vd_saida_btn_close')  # fechar aba venda
    time.sleep(0.5)

    driver.implicitly_wait(10)  # seconds
    click_byxpath('//*[@id="1_grid"]/div/div[3]/div[2]/span[1]/i[3]')  # atualizar
    time.sleep(2)


def run_code(qtds):
    # Loop para realizar os faturamentos
    i = 0
    while i < qtds:
        driver.implicitly_wait(10)  # seconds
        total_itens = driver.find_element(by=By.CLASS_NAME, value='pPageStat').get_attribute("innerHTML").replace(" ",
                                                                                                                  "").replace(
            ".", "").split("/")
        print(total_itens[1] + ' registros restantes' + '\n')
        baixa_faturamento_ativacao()
        i += 1

    else:
        print("Não há faturamento de OS's pendentes")
        driver.quit()
        quit()


# ----------------------------------------------------------------------------------------

login_ixc();

try:
    driver.implicitly_wait(5)  # seconds
    click_byxpath("/html/body/div[8]/vg-modal/div[1]/div[4]/vg-button")
    click_byxpath("/html/body/div[8]/vg-modal/div[2]/div[4]/vg-button[2]")
    time.sleep(2)
except:
    time.sleep(2)

acesso_faturamento_OS();

# Busca a quantidade de registros e realiza split
itens = driver.find_element(by=By.CLASS_NAME, value='pPageStat').get_attribute("innerHTML")
total_itens = itens.replace(" ", "").replace(".", "").split("/");
if itens == "0 itens":
    print("Não há faturamento de OS's pendentes")
    driver.quit()
    quit()
else:
    print(total_itens[1] + ' registros')
    run_code(int(total_itens[1]))
