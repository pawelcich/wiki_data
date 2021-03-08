from bs4 import BeautifulSoup
import requests as r


class NoWikiTableError(Exception):
    pass


def find_country_links(url) -> []:

    page = r.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    links_to_scrape = []
    results = soup.find('div', class_='div-col')

    links = results.find_all('li')
    for link in links:
        l = link.find('a')['href']
        links_to_scrape.append('https://en.wikipedia.org'+str(l))
    return links_to_scrape


def get_country_name(url) -> str:
    # Get country name
    if str(url).find('the_') == -1:
        country = url[str(url).find('in_')+3:]
    else:
        country = url[str(url).find('the_')+4:]
    return country


def get_holiday_details(url) -> []:

    page = r.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find('table', class_='wikitable')
    details = []
    if results:
        hol_details = results.find_all('tr')
        for row in hol_details:
            cols = row.find_all('td')
            cols = [x.text.strip() for x in cols]
            details.append(cols)
        print(f'Details collected for country: {get_country_name(url)}')
        return details[1:]
    else:
        raise NoWikiTableError
