import urllib.request as req
import bs4

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
            print(title.a.string)
            
    push = root.find_all("div", class_="nrec")
    for nrec in push:
        if nrec.span != None:
            print(nrec.span.string)
    
    for title in titles:
        if title.a != None:
            print("https://www.ptt.cc"+ title.a.get("href"))
    


    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]

pageURL = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 3:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1
