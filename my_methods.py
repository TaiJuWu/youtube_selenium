from pytube import YouTube
import pytube
import os
import time
import threading


# url = 'https://www.youtube.com/watch?v=ul-STxaJqKk&t=3s'

def get_vedio(url):
    dir_path = os.getcwd() + '\\crawler_video'
    print('download ' + url + 'and  file output in ' + dir_path)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    try:
        YouTube(url=url).streams.filter(progressive=True).order_by('resolution').desc().first().download(output_path=dir_path)
    except pytube.exceptions.RegexMatchError:
        pass

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


def split_list(download_urls ,i):
    #每i個url分一組，並儲存在download_lists中，格式為[[1,2,3],[4,5,6]。。]
    download_lists = []
    while len(download_urls):
        temp = []
        sp = i
        while True:
            sp = sp -1
            temp.append(download_urls.pop(0))
            if sp == 0 or len(download_urls) == 0:
                break
        download_lists.append(temp)
    return download_lists
    # print(download_lists)

