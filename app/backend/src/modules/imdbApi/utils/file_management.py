import re
import json
import os

def create_file_path(movie_data, path):
    title = re.sub('[^a-zA-Z0-9 \n\.]', '', movie_data['title'])
    year = str(movie_data['year'])
    imdbId = movie_data['id']
    filename = '_'.join([title, year, imdbId]) + '.json'
    filepath = path + filename
    return filepath

def save_movie_data(movie_data, filepath):    
    try:
        with open(filepath, 'w') as movie_file:
            json.dump(movie_data, movie_file, indent=4)
    except:
        print('error')

def load_file(path):
    with open(path, 'r') as file:
        movie = json.load(file)
    return movie 

def load_files(path):
        movies = []
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for file in files:
            filepath = os.path.join(path, file)
            with open(filepath, 'r') as obj:
                movie = json.load(obj)
            movies.append(movie)
        return movies

