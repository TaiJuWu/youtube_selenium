from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
import my_methods as my
import os
from bs4 import BeautifulSoup
import multiprocessing.pool as p
import threading
import time


if __name__ =='__main__':
    start_time = time.time()
    #得到html code
    driver_path = os.path.join(os.getcwd() ,crawler_vedio)
    url = "https://www.youtube.com/user/mycgb2012/videos"
    driver = webdriver.Chrome(executable_path = driver_path)
    driver.get(url)
    time.sleep(1)
    my.scroll(driver ,7)
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
            log = 'youtube_download_log.txt'
            with open(log ,'a+' ,encoding='utf-8') as fp:
                fp.write('tag:\r\n' + str(tag) + '\r\n' + 'error message:\r\n' + str(err) + '='*30 + '\r\n')
    # print(download_urls)
    
    #將download_urls每3個分為一組
    download_lists = my.split_list(download_urls ,2)
    
    #創建process pool
    #本來使用8個process現在改用2個process
    pool =p.Pool(processes=2)
    for download_list in download_lists:
        print('將' ,download_list ,'放入pool中')
        pool.apply_async(my.process_create_thread_to_downlad , args = (download_list,))
        time.sleep(5)
    #關閉pool，防止新的工作進入pool，同時等待子進程完成
    pool.close()
    print('關閉pool')
    pool.join()
    end_time = time.time()
    spend = end_time - start_time
    hour = spend // 3600
    minu = (spend - 3600 * hour) // 60
    sec = spend - 3600 * hour - 60 * minu
    print('全部檔案已下載完成，共花了{0}小時{1}分{2}秒'.format(str(hour),str(minu),str(sec)))
    os.system('pause')


