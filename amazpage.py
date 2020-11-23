from requests_html import HTMLSession
from bs4 import BeautifulSoup


s = HTMLSession()

url = 'https://www.amazon.co.uk/s?k=dslr+camera&i=black-friday&ref=nb_sb_noss'

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('ul', {'class': 'a-pagination'})
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.co.uk' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return


while True:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url)
