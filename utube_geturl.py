from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
from utube_download import get_vedio
import random
import os
import time
from bs4 import BeautifulSoup
import multiprocessing.pool as p
import threading



def scroll(driver ,scroll_time):
    count = 0
    while True:
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, " + str(32000 * count) + ")")
        count = count +1
        scroll_time = scroll_time -1
        if not scroll_time :
            break


# #取消使用這個方法，太慢了
# def open_windows_and_get_url(driver ,download_content):
#     #其他人的Code
#     # action = ActionChains(driver)
#     # action.context_click(download_content).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
#     #我的code
#     # time.sleep(2) #沒有用
#     action = ActionChains(driver)
#     action.move_to_element(download_content)
#     action.context_click()
#     # action.click()  #變成在原本視窗跳轉
#     action.pause(1)
#     action.send_keys(Keys.ARROW_DOWN)
#     action.send_keys(Keys.CONTROL ,'k')
#     action.send_keys(Keys.ENTER)
#     action.perform()
#     time.sleep(random.randrange(1,5))
    
#     driver.switch_to_window(driver.window_handles[1])
#     global download_url
#     download_url = driver.current_url
#     driver.close()
#     time.sleep(1)
#     driver.switch_to_window(driver.window_handles[0])
#     # print('現在的url' , driver.current_url)
#     # driver.forward() 記得在main中加入此動作

#download_lists格式為[1,2,3]
def process_create_thread_to_downlad(download_list):
    threads = []
    for download in download_list:
        thread = threading.Thread(target = get_vedio ,args=(download,))
        thread.start()
        threads.append(thread)
        time.sleep(1)
    for thread in threads:
        thread.join()





if __name__ =='__main__':
    #得到html code
    driver_path = r"C:\Users\User\Desktop\chromedriver.exe"
    url = "https://www.youtube.com/user/mycgb2012/videos"
    start = 5
    video_number = 79
    driver = webdriver.Chrome(executable_path = driver_path)
    driver.get(url)
    time.sleep(random.randrange(1,5))
    scroll(driver ,7)
    #這裡得到的是經過ajax加載的html而不是source code
    html = driver.page_source
    driver.quit()
    # html = etree.parse(html ,parse=parse) #這裡發生錯誤，已經被放棄了
    #採用bs4解析
    domain_name = 'https://www.youtube.com'
    html = BeautifulSoup(html ,'lxml')
    download_tags = html.find_all('a' ,attrs={'class' : 'yt-simple-endpoint inline-block style-scope ytd-thumbnail'})
    download_urls = []
    for tag in download_tags:
        try:
            download_urls.append(domain_name + tag['href']) 
        except KeyError as err:
            pass
    # print(download_urls)
    
    # #每i個url分一組，並儲存在download_lists中，分為格式為[[1,2,3],[4,5,6]。。]
    download_lists = []
    while len(download_urls):
        temp = []
        i = 5
        while True:
            i = i-1
            temp.append(download_urls.pop(0))
            if i == 0 or len(download_urls) == 0:
                break
        download_lists.append(temp)
    print(download_lists)


    #創建process pool
    pool =p.Pool()
    for download_list in download_lists:
        pool.apply_async(process_create_thread_to_downlad , args = (download_list,))
        time.sleep(5)
        print('創建了一個process下載' ,download_list)
    #關閉pool，防止新的工作進入pool，同時等待子進程完成
    pool.close()
    pool.join()
        

    os.system('pause')


