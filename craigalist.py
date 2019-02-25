from urllib.request import urlopen as url  # importing urllib for url request
from bs4 import BeautifulSoup as soup
import re

# my_url = 'https://pittsburgh.craigslist.org/search/apa?query=Perry+North&availabilityMode=0&sale_date=all+dates'
# request = url(my_url)
# htmlscrap = request.read()
# request.close()
# page_soup = soup(htmlscrap, "html.parser")  # parsing as html


# get the search result page


def open_url(args):
    try:
        iter(args)
        result_ = []
        for i in args:
            # print(i)
            open_request = url(i)
            html_scrap = open_request.read()
            # open_request.close()
            house_page = soup(html_scrap, 'html.parser')
            try:
                address = house_page.find('div', {'class': 'mapaddress'}).get_text()
                result_.append(address)
            except AttributeError:
                result_.append('N/A')
            # print(i)
            # print(address)

        # print(i for i in result_)
        # result = [i.get_text() for i in result_]
        return result_
    except TypeError:
        return 'not data'


# container = page_soup.find('ul', {'class': 'rows'})
# result_rows = container.findAll('li', {'class': 'result-row'})
# result_name = [i.find('a', {'class': 'result-title hdrlnk'}).get_text() for i in result_rows]
# result_price = [i.find('span', {'class': 'result-price'}).get_text().lstrip('$') for i in result_rows]
# url_rows = [i.find('a').get('href') for i in result_rows[: 30]]
# # print(result_name)
# result_address = open_url(url_rows)
# print(result_address)
# what we need: name, address, price, url

#
# param: neighbor - name of each neighbor
def scrp_craigs(neighbor):
    neighbor = neighbor.replace(' ', '+')
    my_url = 'https://pittsburgh.craigslist.org/search/apa?query=' + neighbor + '&availabilityMode=0&sale_date=all+dates'
    # print(my_url)
    request = url(my_url)
    htmlscrap = request.read()
    request.close()
    page_soup = soup(htmlscrap, "html.parser")  # parsing as html
    container = page_soup.find('ul', {'class': 'rows'})
    result_rows = container.findAll('li', {'class': 'result-row'})
    names = [i.find('a', {'class': 'result-title hdrlnk'}) for i in result_rows[0:50]]
    prices = [i.find('span', {'class': 'result-price'}) for i in result_rows[0:50]]
    url_rows = [i.find('a').get('href') for i in result_rows[: 50]]
    result_name = []
    result_price = []
    for i in names:
        try:
            result_name.append(i.get_text())
        except AttributeError:
            result_name.append('N/A')
    for i in prices:
        try:
            result_price.append(i.get_text().lstrip())
        except AttributeError:
            result_price.append('N/A')



    # print(result_name)
    result_address = open_url(url_rows)
    result = []
    for i in range(len(result_name)):
        result.append([result_name[i], result_price[i], result_address[i], url_rows[i]])
    return result

#testcase
# neighbor_name = 'Shadyside'
# # print(scrp_craigs(neighbor_name)[0])
# result = scrp_craigs(neighbor_name)
# for i in result:
#     print(i)

# what we need: name, address, price, url
