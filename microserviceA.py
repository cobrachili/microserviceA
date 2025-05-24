import time
import random
import csv

genre_list = ['action', 'strategy', 'adventure', 'casual', 'indie', 'rpg']

def process_csv(input_file, genre=None):
    with open(input_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        games = []
        genreset = set()
        random_genre_list = []
        for row in reader:
            if genre is None:
                games.append(row)
            if genre is not None:
                games.append(row)
                # genreset.add(row.get('genre'))
        if games == []:
            return []
        if genre is not None:
            print("recieved random game csv:\n")
            print(f"{games}\n")
            # print(genreset)
            # random_genre = random.choice(list(genreset))
            random_genre = random.choice(genre_list)
            print(f"random genre is: {random_genre}\n")
            for game in games:
                if game.get('Genre') == random_genre:
                    random_genre_list.append(game)
            # print(random_genre_list)
            return random_genre_list
        # print(genreset)
        # print(games)  
    return games

def write_game_csv(game):
    with open('game.csv', 'w', newline='') as gamefile:
        fieldnames = ['Name', 'Genre', 'Rating', 'Release year']
        writer = csv.DictWriter(gamefile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(game)

while True:
    time.sleep(1)

    randomgame = process_csv('random.csv')
    if randomgame:
        print(f"recieved random game csv:\n")
        print(f"{randomgame}\n")

        recommendation = random.choice(randomgame)
        print(f"\nchosen: {recommendation}\n")
        write_game_csv(recommendation)
        with open('random.csv', 'w'):
            pass

    randomgame_new = process_csv('random_new.csv')
    if randomgame_new:
        print(f"recieved new random game csv:\n")
        print(f"{randomgame_new}")
        recommendation_new = random.choice(randomgame_new)
        print(f"\nchosen: {recommendation_new}\n")
        write_game_csv(recommendation_new)
        with open('random_new.csv', 'w'):
            pass

    randomgame_genre = process_csv('random_genre.csv', genre=True)
    if randomgame_genre:
        recommendation_genre = random.choice(randomgame_genre)
        print(f"\nchosen: {recommendation_genre}\n")
        write_game_csv(recommendation_genre)
        with open('random_genre.csv', 'w'):
            pass  

