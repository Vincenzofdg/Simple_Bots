from tools.browser_settings import create_browser
from tools.env_info import url, user, password
from actions.login import login
from actions.search_profile import search_user as search
from tools.system import clear
from tools.browser_settings import webdriver as web

web = create_browser(test=True)

user_params = [url, user, password, web]
clear()

# user interaction:
user_to_search = input('User to search: ')
number_os_likes = int(input('Quantidades de fotos: '))
type_of_likes = input('\nCurir fotos \n[s] Sequencialmente \n[a] Aleatoriamente\nResposta: ')


def action_function(type):
    print("Login into Instagram")
    login(user_params, False)

    print("Starting search...")
    search(user_to_search, web, url, type)

    web.close()


if type_of_likes == 's':
    action_function(True)
else:
    action_function(False)


# clear()
# print("Action Completed!")