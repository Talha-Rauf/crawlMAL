import requests
from bs4 import BeautifulSoup


def search_anime(a_name):
    a_name = a_name.replace(' ', '%20')
    a_url = f'https://myanimelist.net/search/all?q={a_name}&cat=all'
    anime_code = requests.get(a_url)
    plain_text = anime_code.text  # Converts all the source code into simple text
    soup = BeautifulSoup(plain_text, 'lxml')  # Converts to BeautifulSoup Object
    count = 1
    anime_dict = {}

    for link in soup.find('article').find_all('a', {'class': 'fw-b'}):
        alink = link.get('href')  # Link to each anime
        anime_title = link.string  # Title of each anime
        print(str(count) + ' - ' + anime_title)
        anime_dict[count] = alink  # Dictionary to save links
        count += 1
        if count > 5:
            break

    return anime_dict
