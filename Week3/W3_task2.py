import urllib.request as req
import bs4
import requests

def getData(url):
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")

    for title in titles:
        if title.a != None:
            movie_title = title.a.string
            if "公告" in movie_title:
                continue
            else:
                movie_titles = movie_title
            print(movie_titles)
            
    push = root.find_all("div", class_="nrec")
    for nrec in push:
        if nrec.span != None:
            movie_push = nrec.span.string
            print(movie_push)
                
    for title in titles:
        if title.a != None:
            content_url = "https://www.ptt.cc"+ title.a.get("href")
            res = requests.get(content_url)
            soup = bs4.BeautifulSoup(res.text, "html.parser")

            data_tag = soup.select_one('#main-content > div:nth-child(4) > span.article-meta-value')
            if data_tag:
                date = data_tag.text
                if "2021" in date:
                    continue
                else:
                    dates = date
                print(dates)
                
    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


pageURL = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
all_movie_data = []

while count < 3:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1
