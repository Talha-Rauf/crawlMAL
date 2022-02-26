import requests
from bs4 import BeautifulSoup


def get_single_anime_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text  # Converts all the website code into simple text
    soup = BeautifulSoup(plain_text)
    anime_genre = ''
    anime_studio = ''

    anime_name = soup.find('h1', {'class': 'title-name'}).get_text()

    print(anime_name)
    anime_rating = soup.find('div', {'class': 'score-label'}).get_text()

    print(anime_rating)
    for spaceit_pad in soup.find('div', {'class': 'leftside'}).find_all('div', {'class': 'spaceit_pad'}):

        for span in spaceit_pad.find_all('span'):

            if span.get_text() == 'Studios:':

                for a_studio in spaceit_pad.find_all('a'):
                    anime_studio = anime_studio + a_studio.get_text() + ' '

            if span.get_text() == 'Genres:':

                for a_genre in spaceit_pad.find_all('a'):
                    anime_genre = anime_genre + a_genre.get_text() + ' '

    print(anime_studio.replace('\n', ''))
    print(anime_genre.replace('\n', ''))
    for rightside in soup.find_all('div', {'class': 'rightside'}):
        anime_synopsis = rightside.find('p').get_text()
        anime_review_rating = rightside.select('div.mb8')[0].select('div')[2].get_text()

        review_user = rightside.select_one('div.spaceit .mb8 + div table').select('td')[1].a.get_text()
        anime_review = rightside.select_one('div.spaceit.textReadability').get_text()

    print(review_user.replace('\n', ''))
    print(anime_review.replace('\n', ''))
    print(anime_review_rating.replace('\n', ''))

    return [anime_name, anime_rating, anime_studio, anime_genre, anime_synopsis, review_user, anime_review_rating,
            anime_review]
