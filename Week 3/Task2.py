import requests
from bs4 import BeautifulSoup
url="https://www.ptt.cc/bbs/Food/index.html"
    
def get_all_href(url):
    r = requests.get(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    soup = BeautifulSoup(r.text, "lxml")
    results = soup.select("div.title")
    for item in results:
        a_item = item.select_one("a")
        if a_item:
            get_article_content(article_url='https://www.ptt.cc'+a_item.get('href'))
    print('------------------ next page ------------------')
    
for page in range(1,4):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    btn = soup.select('div.btn-group > a')
    if btn:
        next_page_url = 'https://www.ptt.cc' + btn[3]['href']
        url = next_page_url
        print('page:', url)
        get_all_href(url = url)

# def get_article_content(article_url):
#     r = requests.get(article_url)
#     soup = BeautifulSoup(r.text, "lxml")
#     r = requests.get(article_url)
#     soup = BeautifulSoup(r.text, "lxml")
#     results = soup.select('span.article-meta-value')
#     if results:
#         print('作者:', results[0].text)
#         print('看板:', results[1].text)
#         print('標題:', results[2].text)
#         print('時間:', results[3].text)