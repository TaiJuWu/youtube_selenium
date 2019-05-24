from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
from utube_download import get_vedio
import random
import os
import time


download_url = ''

def scroll(driver ,scroll_time):
    while True:
        time.sleep(random.randrange(1,5))
        driver.execute_script("window.scrollTo(0, 32000)")
        scroll_time = scroll_time -1
        if not scroll_time :
            break

def open_windows_and_get_url(driver ,download_content):
    #其他人的Code
    # action = ActionChains(driver)
    # action.context_click(download_content).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    #我的code
    # time.sleep(2) #沒有用
    action = ActionChains(driver)
    action.move_to_element(download_content)
    action.context_click()
    # action.click()  #變成在原本視窗跳轉
    action.pause(1)
    action.send_keys(Keys.ARROW_DOWN)
    action.send_keys(Keys.CONTROL ,'k')
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(random.randrange(1,5))
    
    driver.switch_to_window(driver.window_handles[1])
    global download_url
    download_url = driver.current_url
    driver.close()
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[0])
    # print('現在的url' , driver.current_url)
    # driver.forward() 記得在main中加入此動作




if __name__ =='__main__':
    driver_path = r"C:\Users\User\Desktop\chromedriver.exe"
    url = "https://www.youtube.com/user/mycgb2012/videos"
    start = 5
    video_number = 79
    driver = webdriver.Chrome(executable_path = driver_path)
    driver.get(url)
    time.sleep(random.randrange(1,5))
    xpath_parse = '//ytd-grid-renderer[contains(@class,"ytd-item-section-renderer")]/div[contains(@class ,"ytd-grid-renderer")]/ytd-grid-video-renderer[{0}]'
    for i in range(start ,video_number):
        download_element = driver.find_element_by_xpath(xpath_parse.format(str(i)))
        # scroll(driver ,10)
        open_windows_and_get_url(driver ,download_element)
        print(download_url)
        time.sleep(1)

    os.system('pause')


