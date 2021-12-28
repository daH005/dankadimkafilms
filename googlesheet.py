import gspread
from random import randint


# Google-таблица
class GoogleSheet:
    def __init__(self, credentials):
        gc = gspread.service_account_from_dict(credentials)
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1tD85Jzvsg0zTmFqarYvH7MgHVKiogG8Wl-4cFbopIu0/edit#gid=0')
        self.worksheet = sh.get_worksheet(0)    

    def __get_col_values(self, col):
        return self.worksheet.col_values(col)[1:]

    def get_random_film(self):
        films = self.__get_col_values(1)
        danil_agree = self.__get_col_values(2)
        dima_agree = self.__get_col_values(3)
        views = self.__get_col_values(4)

        if self.get_not_viewed_films_amount() != 0:
            while True:
                try:
                    random_index = randint(0, len(films)-1)
                    if danil_agree[random_index].lower() == 'да' and dima_agree[random_index].lower() == 'да' and views[random_index].lower() != 'да':
                        return films[random_index]
                except:
                    pass

        return None

    def get_all_films(self):
        return '\n'.join(self.__get_col_values(1))

    def get_viewed_films(self):
        films = self.__get_col_values(1)
        views = self.__get_col_values(4)

        viewed_films = []
        for i in range(len(films)):
            try:
                if views[i] == 'да':
                    viewed_films.append(films[i])
            except:
                break

        return '\n'.join(viewed_films)

    def get_not_viewed_films(self):
        films = self.__get_col_values(1)
        views = self.__get_col_values(4)

        not_viewed_films = []
        for i in range(len(films)):
            try:
                if views[i] != 'да':
                    not_viewed_films.append(films[i])
            except:
                not_viewed_films.append(films[i])

        return '\n'.join(not_viewed_films)

    def get_all_films_amount(self):
        return len(self.get_all_films().splitlines())

    def get_viewed_films_amount(self):
        return len(self.get_viewed_films().splitlines())

    def get_not_viewed_films_amount(self):
        return len(self.get_not_viewed_films().splitlines())