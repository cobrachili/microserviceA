# microserviceA
361 microservice for Conrad

# How to request data
There are three cases that the microservice will respond to. Each case requires that a csv with the headers game_title, played, and genre is printed to the specified .csv file.

Case 1) The user wants a random game, so they write a csv of games to the random.csv file

Case 2) The user wants a random game they have not play played before, so they write a csv to the random_new.csv file

Case 3) The user wants a random game by a random genre, so they write a csv to the random_genre.csv file.

# Example call
```
games = "game_title,played,genre
fortnite,false,battle royale
league of legends,true,moba
counter-strike,true,first-person shooter
super mario,false,platformer"
```
Case 1) Random game:
```
def write_game_csv(games):
    with open('random.csv', 'w', newline='') as gamefile:
        fieldnames = ['game_title', 'played', 'genre']
        writer = csv.DictWriter(gamefile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(games)
```
Case 2) New random game
```
def write_game_csv(games):
    with open('random_new.csv', 'w', newline='') as gamefile:
        fieldnames = ['game_title', 'played', 'genre']
        writer = csv.DictWriter(gamefile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(games)
```
Case 3) Random game by random genre
```
def write_game_csv(games):
    with open('random_genre.csv', 'w', newline='') as gamefile:
        fieldnames = ['game_title', 'played', 'genre']
        writer = csv.DictWriter(gamefile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(games)
```
# How to recieve data
Each time the client makes a request to have a random game reccomendation they must read from the game.csv file. The game.csv file will contain the headers game_title, played, and genre along with one entry which is the random game. 

# Example call
```
with open(input_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        games = []
        for row in reader:
                games.append(row)
    return games
```
# UML Sequence Diagram 
![image](https://github.com/user-attachments/assets/8dd640c7-ac5b-49c7-a9bf-74611f767117)


