from pytube import YouTube
import pytube
import os


# url = 'https://www.youtube.com/watch?v=ul-STxaJqKk&t=3s'

def get_vedio(url):
    dir_path = os.getcwd() + '\\crawler_video'
    print('file output in ' + dir_path)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    YouTube(url=url).streams.first().download(output_path=dir_path)
try:
    get_vedio('https://www.youtube.com/user/mycgb2012/featured')
except pytube.exceptions.RegexMatchError as err:
    print('123')