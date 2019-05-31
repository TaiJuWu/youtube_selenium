from pytube import Playlist


if __name__ == '__main__':
    url = input('請輸入下載的url:  ')
    path = input('請輸入儲存的path:  ')
    dow = Playlist(url = url)
    dow.download_all(download_path=path)
