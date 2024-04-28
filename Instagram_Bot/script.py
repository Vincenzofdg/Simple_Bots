from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from dotenv import dotenv_values
from tools.system import clear
from actions.login import login
from actions.visite_user import visite_user as visite
from time import sleep

# Browser Settings
# setting = Options()
# setting.add_argument("--disable-extensions")
# setting.add_argument("--disable-gpu")
# setting.add_argument("--no-sandbox")
# setting.add_argument("--disable-dev-shm-usage")
# setting.add_argument("--headless")

# browser = webdriver.Firefox(options=setting)

browser = webdriver.Firefox()

env = dotenv_values(".env")

user = env["username"]
password = env["password"]
url = env["url_instagram"]

# array_user_test = ["vincenzofdg", "sam_1jz", "kkaio.exe","ofabiobalbino", "cadumaranhao.design","enzocostadev", "rickvinana","edpojc","agatamoreiram","debora.stefanny","suehortas","nataliansantana","gustavineoo"]
array_user_test = ["sam_1jz"]

clear()

print("Ola eu sou o RoboGuide!!\nEstarei realizando as automacoes do sistema.")


n=1
while (n >= 0):
    try:
        login([url, user, password, browser], False)  # Bot login
    except TimeoutException: 
        try:
            login([url, user, password, browser], True)
        except TimeoutException:
            sleep(2)
    finally:
        sleep(2)
        browser.close()

# try:
#    login([url, user, password, browser], False)  # Bot login
# except TimeoutException: 
#     # Mudança do Xpath do input usuario e senha 
#     login([url, user, password, browser], True)
    
# try:
#     for user in array_user_test:  # Visite a User
#         visite([url, user, browser])

#     browser.close()  # Close Browser and Bot
# except KeyboardInterrupt:
#     print("Forcada a parada do programa")
#     browser.close()


