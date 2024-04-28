import web_elements.new_elements as style
from selenium.webdriver.common.by import By
from tools.selenium_functions import xpath
import time

def search_user(user, web, url, condition):

    web.get(url + user)

    num_of_posts = xpath(style.xpath_num_of_posts, web)
    qtd_post = num_of_posts.text
    rows = int(qtd_post) / 3

    photo = xpath(style.xpath_single_photo(3, 2), web)
    photo.click()




    time.sleep(15)

    # /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]
    # /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[2]/div[1]
    # /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[9]/div[2]








