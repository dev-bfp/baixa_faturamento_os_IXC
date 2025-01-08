import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime

options = Options()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches", ["enable-automation"])


def search_local_file(folder, file_name):
    for file in folder:
        caminho = os.path.join(file, file_name)
        if os.path.exists(caminho):
            print(f'Caminho Chromedriver: {caminho}')
            return caminho
    print("Arquivo não encontrado em nenhuma das pastas.")
    return None


caminhos = [r"C:\Users\DEV\Desktop\EXE", r"C:\Users\Financeiro\OneDrive\dev-bfp\GitHub\IXC - baixa_faturamento_os"]  # PC Stive | PC Brian
link_webdriver = search_local_file(caminhos, 'chromedriver.exe')

driver = webdriver.Chrome(options=options, service=Service(link_webdriver))
driver.implicitly_wait(20)  # seconds


# ----------- find element by id -----------
def click_byid(id):
    driver.find_element(by=By.ID, value=id).click()


def send_byid(id, txt):
    driver.find_element(by=By.ID, value=id).send_keys(txt)


def clear_byid(id):
    driver.find_element(by=By.ID, value=id).clear()


def get_info_byid(id, atributo="innerHTML"):
    driver.find_element(by=By.ID, value=id).get_attribute(atributo)


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
    link = 'https://crm.redfibra.com.br/adm.php'
    driver.get(link)
    driver.maximize_window()

    send_byid('email', 'automacao@redfibra.com.br')  # insere email
    click_byid('btn-next-login')
    time.sleep(1)
    send_byid('password', 'G1W!q4te29LX')  # insere senha
    click_byid('btn-enter-login')  # clica em entrar
    time.sleep(1)
    try:
        click_byid('btn-enter-login')  # clica em entrar
        driver.implicitly_wait(20)  # seconds
        try:
            click_byxpath('//*[@id="slide_0"]/div[1]/i')  # fecha pop-up
            try:
                click_byid('closeButton')
                time.sleep(1)
            except:
                pass
        except:
            time.sleep(1)

    except:
        try:
            click_byxpath('//*[@id="warning"]/vg-body/div/vg-button[2]')  # fecha pop-up
        except:
            time.sleep(1)
            print('Erro login')
            driver.quit()


def acesso_faturamento_OS():
    driver.implicitly_wait(20)  # seconds
    click_byid('id_input_menu')  # abre pesquisa
    send_byid('id_input_menu', 'pedido')  # insere pesquisa
    click_byxpath('//*[@id="grupo_menu1d86c02f14a5c80984dc87f3187c0396"]/ul/li[3]/ul/li[3]/a')  # acessa menu pedido de ordem de serviço
    time.sleep(2)
    click_byxpath('//*[@id="1_grid"]/div/div[4]/div[1]/span[2]/i')  # abre menu da grid
    click_byxpath('//*[@id="1_grid"]/div/div[4]/nav[2]/ul/li')  # insere filtro salvo
    time.sleep(2)


def baixa_faturamento_ativacao():
    click_byname('btn_finalizar_pedido')  # finalizar pedido
    print("botão finalizar pedido")
    time.sleep(2)

    filial = driver.find_element(by=By.ID, value='filial_id').get_attribute('value')

    driver.implicitly_wait(20)  # seconds
    click_byid('previsaoN')  # insere previsão "não"
    print("botão previsão N")
    time.sleep(0.1)

    driver.implicitly_wait(20)  # seconds
    click_byxpath('//*[@id="2_form"]/div[2]/button[2]')  # save
    print("save")
    time.sleep(0.5)

    driver.implicitly_wait(20)  # seconds
    click_byid('finalizar_saida')  # finalizar saida
    print("botão finalizar saida")
    time.sleep(1.5)

    driver.implicitly_wait(20)  # seconds
    carteira_cobranca = '1' if filial == "1" else "8"
    send_byid('id_carteira_cobranca', carteira_cobranca)  # inserir carteira de cobrança
    print("inserir carteira de cobrança")

    driver.implicitly_wait(20)  # seconds
    send_byid('id_carteira_cobranca', Keys.TAB)  # TAB no campo
    print("tab")
    time.sleep(1)

    driver.implicitly_wait(20)  # seconds
    click_byxpath('//*[@id="3_form"]/div[2]/button[1]')  # salvar e gerar financeiro
    print("botão salvar e gerar financeiro")

    driver.implicitly_wait(20)  # seconds
    click_byid('validar_finalizar')  # validar e finalizar
    print("botão validar e finalizar")

    driver.implicitly_wait(20)  # seconds
    click_byid('vd_saida_fechamento_btn_close')  # fechar aba
    print("botão fechar aba fechamento")
    time.sleep(0.5)

    driver.implicitly_wait(20)  # seconds
    click_byid('vd_saida_btn_close')  # fechar aba venda
    print("botão fechar aba venda")
    time.sleep(0.5)

    driver.implicitly_wait(20)  # seconds
    click_byxpath('//*[@id="1_grid"]/div/div[4]/div[2]/span[1]/i[3]')  # atualizar
    print("botão atualizar")
    time.sleep(2)


def run_code(qtds):
    i = 0
    while i < int(qtds):
        driver.implicitly_wait(20)  # seconds
        try:
            registros = driver.find_element(by=By.XPATH, value='//*[@id="1_grid"]/div/div[4]/div[2]/span[2]')
            registros.get_attribute("innerHTML").replace(" ", "").replace(".", "").split("/")
            print(registro1[1] + ' registros restantes' + '\n')
        except:
            pass
        baixa_faturamento_ativacao()
        i += 1

    else:
        print("-")
        print("-")
        print("-")
        print("Fim")


# ----------------------------------------------------------------------------------------

login_ixc();
acesso_faturamento_OS();

registro1 = driver.find_element(by=By.XPATH, value='//*[@id="1_grid"]/div/div[4]/div[2]/span[2]').get_attribute("innerHTML")
print(registro1)
if registro1 == "0 itens":
    driver.quit()
else:
    registro1 = registro1.replace(" ", "").replace(".", "").split("/");
    print(registro1[1] + ' registros')
    run_code(int(registro1[1]))
    # run_code("10")