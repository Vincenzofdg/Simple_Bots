from tools.browser_settings import create_browser
from selenium.common.exceptions import TimeoutException
from actions.login import login
from actions.create_post import create_post as post
import tools.env_info as env
from tools.system import clear
import schedule
from time import sleep


web = create_browser(test=True)

login_info = [env.url, env.user, env.password, web]

def post_schedule(content, image_name):
    
    try:
        login(login_info, False)
    except TimeoutException:
        login(login_info, True)
    finally:
        post(web, content, image_name)
        web.close()
        print('Posted')

clear()

when_to_run = input('Para que horas desejar agendar o bot? ')

image_name = input('Nome da image colocada no diretorio /Document/Instagram_bot? ')

post_content = input('Qual a descricao do post? ')

clear()

print(f'\n\nPost scheduled at {when_to_run}\n')

schedule.every().day.at(when_to_run).do(lambda: post_schedule(post_content, image_name))


while True:
    schedule.run_pending()
    sleep(1)
    # validar quando o agendamento eh feito e quebrar esse while com return

# web.close()
