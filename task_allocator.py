import random

LINE = "-" * 79
hello = "Welcome to Team Allocator!"

print(f"{LINE}\n{hello}\n{LINE}")
players = ["Steph", "James", "Tonya", "Jonnie", "Lorenzo", "Rubi"]

while True:
    random.shuffle(players)
    response = input("Is it a team or individual sport? \
                    \nType team or individual: ")
    if response == "team":
        team1 = players[:len(players)//2]
        print("Team 1 captain: " + random.choice(team1))
        print("Team 1:")
        for player in team1:
            print(player)
        team2 = players[len(players)//2:]
        print("\nTeam 2 captain: " + random.choice(team2))
        print("Team 2:")
        for player in team2:
            print(player)
       
        response = input("Pick teams again? Type y or n:")
        if response == "n":
            break
