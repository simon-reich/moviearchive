import datetime
import re

def strip_special_characters(string):
    return re.sub('[^a-zA-Z0-9 \n\.]', '', string)


def check_if_string_is_year(string):
    return re.match('[0-9][0-9][0-9][0-9]', string)


def check_if_string_is_releaseYear(string):
        if int(string) > 1950 and int(string) < int(datetime.datetime.now().year):
            return True


def check_if_string_is_runtime(string):
        if int(string) < 350:
            return True
        elif re.search(r'\d+min', string):
            return True


def check_if_string_is_genre(string):
        pass


def year_to_century(year: str):
    year = year.strip()
    if len(year) > 2: 
        year = int(year) + 100
        year = f"{str(year)[:-2]}th" 
        return year

def analyze_query(query: str):
    query = query.strip()