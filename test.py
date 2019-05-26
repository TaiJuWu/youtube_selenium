# urls = [1,2,3,4,5,6,7 ,8,9,10,11,12,13,15,16,7,18,189]
# list_=[]

# while len(urls):
#     temp = []
#     i = 5
#     while True:
#         i = i-1
#         temp.append(urls.pop(0))
#         if i == 0 or len(urls) == 0:
#             break
#     list_.append(temp)
 
# print(list_)

domain_name = 'https://www.youtube.com'
html = BeautifulSoup(html ,'lxml')
download_tags = html.find_all('a' ,attrs={'class' : 'yt-simple-endpoint inline-block style-scope ytd-thumbnail'})
download_urls = []
for tag in download_tags:
    try:
        download_urls.append(domain_name + download_tags['href']) 
    except KeyError as err:
        pass
    print(download_urls)