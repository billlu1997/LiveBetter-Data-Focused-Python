import bs4  # importing soup
from urllib.request import urlopen as url  # importing urllib for url request
from bs4 import BeautifulSoup as soup
import random
import re
import requests
import time


# filename="datasets.txt"  # saving data as csv
# f = open(filename, "w")
# my_url = 'https://www.yelp.com/search?cflt=restaurants&find_near=carnegie-mellon-university-pittsburgh-6&l=g%3A-79' \
#          '.9689674377%2C40.4244739964%2C-79.9178123474%2C40.4636663246 '

#
# param: loc - the location
def restaurant(loc):
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    loc = loc.replace(' ', '%')
    my_url = 'https://www.yelp.com/search?find_desc=&find_loc='+loc+'%2CPittsburgh'
    # print(my_url)
    # time.sleep(30)
    with requests.Session() as s:
        page = s.get(my_url, headers=req_headers)
        # time.sleep(10)
    data = page.content
    data_str = str(data,'utf-8')
    # print(type(data))
    # print(data)
    # file = open('sourcepage.txt', 'w')
    # file.writelines(data)

    # file = open('sourcepage.txt', 'r')
    # print(my_url)
    # try:
    #     request = url(my_url)
    # except:
    #     return [[],[],[],[],[]]
    # request = url(my_url)
    # htmlscrap = request.read()
    # request.close()
    page_soup = soup(data_str, "html.parser")  # parsing as html
    restaurant_name = [i.get_text() for i in page_soup.findAll("a", {"class": "lemon--a__373c0__IEZFH link__373c0__29943 "
                                                       "link-color--blue-dark__373c0__1mhJo "
                                                       "link-size--inherit__373c0__2JXk5"})]

    restaurant_rating =[i.get('aria-label').rstrip(' star rating') for i in page_soup.findAll("div", {"class": re.compile('lemon--div__373c0__1mboc i-stars__373c0__Y2F3O')})]
    # print(len(restaurant_rating))
    # restaurant_address = [i.get_text() for i in page_soup.findAll("address", {'class': 'domtags--address__373c0__cgebO'})]
    # print(len(restaurant_address))

    restaurant_url = ['https://www.yelp.com'+i.get('href') for i in page_soup.find_all("a", {"class": "lemon--a__373c0__IEZFH link__373c0__29943 "
                                                       "link-color--blue-dark__373c0__1mhJo "
                                                       "link-size--inherit__373c0__2JXk5"})]
    # print(len(restaurant_url))
    # restaurant_dist = [i.get_text() for i in page_soup.find_all('span', class_='lemon--span__373c0__3997G display--inline__373c0__1DbOG u-space-l-half border-color--default__373c0__2oFDT', string=re.compile('Miles'))]
    # print(len(restaurant_dist))

    result = [[restaurant_name[i], restaurant_rating[i], restaurant_url[i]] for i in range(len(restaurant_name))]
    return result
    # result = [[restaurant_name[i], restaurant_rating[i], restaurant_address[i], restaurant_dist[i], restaurant_url[i]] for i in range(len(restaurant_name))]


    #output format:
    # restaurant name, restaurant rating, restaurant address, restaurant dist, restaurant url(yelp site)
    # print(re.findall(ratings))


# testate
# if __name__ is '__main__':
# for i in restaurant('515 S Aiken Ave, Pittsburgh, PA'):
#     print(i)
