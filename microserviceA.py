import time
import random
import csv

def process_csv(input_file, played=None, genre=None):
    with open(input_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        games = []
        genreset = set()
        random_genre_list = []
        for row in reader:
            if played is not None and row.get('played') == played:
                games.append(row)
            if played is None and genre is None:
                games.append(row)
            if genre is not None:
                games.append(row)
                genreset.add(row.get('genre'))
        if games == []:
            return []
        if genre is not None:
            # print(genreset)
            random_genre = random.choice(list(genreset))
            for game in games:
                if game.get('genre') == random_genre:
                    random_genre_list.append(game)
            return random_genre_list
        # print(genreset)
        # print(games)  
    return games

def write_game_csv(game):
    with open('game.csv', 'w', newline='') as gamefile:
        fieldnames = ['game_title', 'played', 'genre']
        writer = csv.DictWriter(gamefile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(game)

while True:
    time.sleep(1)

    randomgame = process_csv('random.csv')
    if randomgame:
        recommendation = random.choice(randomgame)
        write_game_csv(recommendation)
        with open('random.csv', 'w'):
            pass

    randomgame_new = process_csv('random_new.csv', played='false')
    if randomgame_new:
        recommendation_new = random.choice(randomgame_new)
        write_game_csv(recommendation_new)
        with open('random_new.csv', 'w'):
            pass

    randomgame_genre = process_csv('random_genre.csv', played=None, genre=True)
    if randomgame_genre:
        recommendation_genre = random.choice(randomgame_genre)
        write_game_csv(recommendation_genre)
        with open('random_genre.csv', 'w'):
            pass  

