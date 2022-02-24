import requests
from bs4 import BeautifulSoup
from singleAnimeData import get_single_anime_data
from searchAnime import search_anime
from saveAnimeData import save_anime_data


while True:
    in_anime_name = input("Type the anime name: ")
    list_anime = search_anime(in_anime_name)
    user_selection = input("The first 5 anime has been listed above.\nChoose an anime using its number: ")
    anime_data = get_single_anime_data(list_anime[int(user_selection)])

    while True:
        choice = input('What would you like to do next?\n1- Save Information\n'
                       '2- Search another anime\n3- Exit the program\nChoose your '
                       'option using its number: ')

        if choice == '1':
            save_anime_data(anime_data)
            print('Information saves successfully. File name is "' + anime_data[0] + '".')
            break
        elif choice == '2':
            break
        elif choice == '3':
            break
        else:
            print('Try again...')
            continue

    if choice == '1' or choice == '3':
        break
