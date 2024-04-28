from tools.selenium_functions import xpath
import web_elements.new_elements as style
import web_elements.mouse_location as coords
from time import sleep
from pyautogui import click, hotkey, press, leftClick, write
from pyperclip import copy
from tools.write_text import write_text
from pyvirtualdisplay import Display

def create_post(web, content, image_name):
    print("Iniciando postagem.")

    btn_create_post = xpath(style.xpath_btn_create_post, web)
    btn_create_post.click()

    btn_select_img = xpath(style.xpath_btn_select_img, web)
    btn_select_img.click()
    
    # LINUX {
    display = Display(visible=False)
    display.start() 
   
    click(*coords.file_path_on_search)
    copy("C:/Users/summer/Documents/Instagram_Bot")
    hotkey("ctrl", "v")
    press("enter")
    sleep(4)
    
    click(*coords.btn_image_name_filter)
    sleep(3)
    write(f'{image_name}.')
    sleep(5)
    press('enter')
    sleep(3)
    leftClick(*coords.image_select)
    press("enter")
    # display.stop()

    btn_img_next = xpath(style.xpath_btn_img_next, web)
    btn_img_next.click()

    btn_img_next = xpath(style.xpath_btn_img_next, web)
    btn_img_next.click()
    
    description_post_01 = xpath(style.xpath_description_post_01, web)
    description_post_02 = xpath(style.xpath_description_post_02, web)
    write_text(description_post_01, description_post_02, content)

    btn_confirm_post = xpath(style.xpath_btn_confirm_post, web)
    btn_confirm_post.click()

    sleep(3)
