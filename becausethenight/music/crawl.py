"""Web crawling and scraping
"""


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep

BASE_URL_IMDB = 'https://www.imdb.com'
BASE_URL_DISCOGS = 'https://www.discogs.com'
BASE_URL_PATTI_SMITH = 'http://www.pattismith.net'


def get_soup(url):
    """Get a BeautifulSoup object from the URL passed as the parameter/argument.

    To encode response text as bytes object, use str.encode(encoding="utf-8", errors="strict").
    From str.encode() documentation: The errors argument specifies the response when the input string can’t be
    converted according to the encoding’s rules. Legal values for this argument are
    'strict' (raise a UnicodeDecodeError exception),
    'replace' (use U+FFFD, REPLACEMENT CHARACTER),
    'ignore' (just leave the character out of the Unicode result), or
    'backslashreplace' (inserts a \\xNN escape sequence).

    The following lines use str.encode() to prepare the text of the response for BeautifulSoup as a bytes object,
    using encoding="utf-8" and errors="replace":

    response_text_bytes = response_text.encode('utf-8', 'replace')
    soup = BeautifulSoup(response_text_bytes, 'html.parser')

    The following line uses the response text directly as a string in the BeautifulSoup constructor
    (encoding="utf-8" and errors="strict" is assumed, hence it can raise a UnicodeDecodeError exception):

    soup = BeautifulSoup(response_text, 'html.parser')

    The following line uses the response text directly as a string, as well as a default HTML parser
    (but issues a warning about it as well):

    soup = BeautifulSoup(response_text)
    """

    response = requests.get(url, allow_redirects=False)
    response_text = response.text
    return BeautifulSoup(response_text, 'html.parser')


def crawl(base_url, get_pages, max_pages=1):
    """Web crawler that collects specific info from the Web.
    Parameters:
        - the url of the starting Web page
        - the function that collects the pages to crawl
        - the max number of pages to crawl in case of multi-page lists
    """

    soups = []
    pages = get_pages(base_url, max_pages)
    for page in pages:
        soup = get_soup(page)
        sleep(1)
        soups.append(soup)
    return soups


def get_imdb_pages(base_url, max_pages=1):
    """Collects specific pages from IMDb.
    Parameters:
        - the url of the starting page (base_url)
        - the max number of pages to collect in case of multi-page lists
    """

    pages = []
    page_counter = 1
    while page_counter <= max_pages:
        page = base_url + str((page_counter - 1) * 50 + 1) + '&ref_=adv_nxt'
        pages.append(page)
        page_counter += 1
    return pages


def crawl_imdb_for_titles_and_links(base_url, max_pages=1):
    """Collects titles and the corresponding links from specific IMDb pages.
    Parameters:
        - the url of the starting page (base_url)
        - the max number of pages to crawl in case of multi-page lists
    """

    soups = crawl(base_url, get_imdb_pages, max_pages)
    for soup in soups:
        list_div = soup.find_all('div', {'class': 'lister-item mode-advanced'})
        for div in list_div:
            title = div.find('h3').find('a').text.lstrip()
            link = urljoin(BASE_URL_IMDB, div.find('h3').find('a').get('href'))
            print('{}\n{}\n'.format(title, link))


def get_patti_smith_albums_pages(base_url, max_pages=1):
    """Collects related pages from a Website that displays info about Patti Smith albums.
    Parameters:
        - the url of the starting page (base_url)
        - the max number of pages to collect in case of multi-page lists
    """


def crawl_patti_smith_albums(base_url, max_pages=1):
    """Collects titles of Patti Smith albums and the corresponding links from Discogs.
    Parameters:
        - the url of the starting page (base_url)
        - the max number of pages to crawl in case of multi-page lists
    """


def get_patti_smith_pages(base_url, max_pages=1):
    """Collects specific pages from a Patti Smith Website (such as her home page).
    Parameters:
        - the url of the starting page (base_url)
        - the max number of pages to collect in case of multi-page lists
    """

    pages = []
    page_counter = 1
    while page_counter <= max_pages:
        page = base_url + '?page=' + str(page_counter)
        pages.append(page)
        page_counter += 1
    return pages


def crawl_patti_smith_home_page(base_url, max_pages=1):
    """Collects relevant links from Patti Smith homepage and from the linked ones.
    Parameters:
        - the url of the starting page (base_url)
        - the max number of pages to crawl in case of multi-page lists
    """

    soups = crawl(base_url, get_patti_smith_pages, max_pages)
    for soup in soups:
        links = soup.find('nav').find_all('a')
        for l in links:
            # title = l.attrs['title'].capitalize()
            title = l.text.capitalize()
            link = urljoin(BASE_URL_PATTI_SMITH, l.get('href'))
            print('{}\n{}\n'.format(title, link))

            soup2 = get_soup(link)
            links2 = soup2.find_all('a')
            for lnk in links2:
                # print('\t{}'.format(lnk.get('href')))
                print('\t{}'.format(urljoin(BASE_URL_PATTI_SMITH, lnk.get('href'))))


if __name__ == "__main__":

    # Some links to play with

    # patti_smith_homepage = "http://www.pattismith.net"
    # patti_smith_facebook_page = "https://www.facebook.com/PattiSmithAuthor/"
    # patti_smith_albums = 'https://www.discogs.com/artist/193816-Patti-Smith'
    # patti_smith_five_essential_albums = start_url = \
    #     'https://theculturetrip.com/north-america/usa/new-york/articles/five-essential-patti-smith-albums/'
    # because_the_night_40_anniversary_page = \
    #     'https://www.billboard.com/articles/columns/rock/8462017/' \
    #     'patti-smith-because-the-night-40th-anniversary-oral-history'

    # Intro

    # patti_html = \
    #     """<h1>Patti Smith</h1>\
    #     <p>This is her <a href="http://www.pattismith.net">home page</a></p>
    #     <p>This is her <a href="https://www.facebook.com/PattiSmithAuthor/">Facebook page</a></p>
    #     """
    # soup = BeautifulSoup(patti_html, 'html.parser')
    #
    # # the soup object (print it, print its type, print its text attribute)
    #
    # print(soup)
    # print(type(soup))
    # print(soup.text)
    #
    # # find() and tags (examples: 'a', 'p', 'h1'; print them, print their types, print their text attributes)
    # print(soup.find('a'))
    # print(soup.find_all('a'))
    # print(soup.find_all('p'))
    #
    # # attrs (print attrs of some tags, as well as specific attrs (such as attrs['href']))
    # print(soup.find('a').attrs)
    # print(soup.find('a').get('href'))
    # print()
    #
    #
    # # find_all() (example: soup.find_all('a'))
    # # print href and text attrs for a link (link.get(), link.attrs[], link.string, link.text)

    print()

    # Test crawl functions

    # crawl_imdb_for_titles_and_links('https://www.imdb.com/search/title?title=Bruce%20Springsteen&start=', 1)
    # soup = get_soup('http://www.pattismith.net/intro.html')
    # print(str(soup)[:500])
    crawl_patti_smith_home_page('http://www.pattismith.net/intro.html')

    # pages = get_imdb_pages('https://www.imdb.com/search/title?title=Bruce%20Springsteen&start=', 3)
    # for page in pages:
    #     print(page)

    # soup = get_soup('https://www.imdb.com/search/title?title=Bruce%20Springsteen&start=1&ref_=adv_nxt')
    # print(str(soup)[:500])

    # soups = crawl('https://www.imdb.com/search/title?title=Bruce%20Springsteen&start=', get_imdb_pages, 2)
    # print(len(soups))
    # print(str(soups[0])[:500])
    # print()
    # # print(soups[0].find('div', {'class': 'lister-item mode-advanced'}))
    # # print(soups[0].find('div', {'class': 'lister-item mode-advanced'}).find('h3').find('a'))
    # print(soups[0].find('div', {'class': 'lister-item mode-advanced'}).find('h3').find('a').text)
    # # print(soups[0].find('div', {'class': 'lister-item mode-advanced'}).find('h3').find('a').attrs['href'])
    #
    # # Working with relative links
    #
    # BASE_URL = 'https://www.imdb.com'
    # rel_lnk = soups[0].find('div', {'class': 'lister-item mode-advanced'}).find('h3').find('a').attrs['href']
    # print(urljoin(BASE_URL, rel_lnk))

    # crawl_imdb_for_titles_and_links('https://www.imdb.com/search/title?title=Bruce%20Springsteen&start=', 3)
    # crawl_patti_smith_albums('https://www.discogs.com/artist/193816-Patti-Smith', 3)
    # crawl_patti_smith_home_page('http://www.pattismith.net/intro.html')


