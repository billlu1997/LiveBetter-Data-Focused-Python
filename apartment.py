from bs4 import BeautifulSoup as soup
import requests
import re

# param: neighbor - return a list of the first result page


def scrp_apartment(neighbor):
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    neighbor = neighbor.replace(' ', '-')
    my_url = 'https://www.apartments.com/'+neighbor+'-pa/?bb=iojnprr5nIyg4tuD'
    with requests.Session() as s:
        page = s.get(my_url, headers=req_headers)
    data = page.content
    page_soup = soup(data, "html.parser")  # parsing as html
    price = [i.get_text() for i in page_soup.find_all('span', {'class': 'altRentDisplay'})]
    name = [i.get_text().lstrip('\r\n') for i in page_soup.find_all('a', {'class': re.compile('placardTitle js-placardTitle')})]
    urls = [i.get('href') for i in page_soup.find_all('a', {'class': re.compile('placardTitle js-placardTitle')})]
    address = [i.get('title') for i in page_soup.find_all('div', {'class': 'location'})]

    result = []
    for i in range(len(name)):
        result.append([name[i], price[i], address[i], urls[i]])
    return result

#
# for i in scrp_apartment('shadyside'):
#     print(i)
