blocks=["-" for i in range (9)]

def display_game():
    print("|",blocks[0],"|",blocks[1],"|",blocks[2],"|")
    print("|",blocks[3],"|",blocks[4],"|",blocks[5],"|")  
    print("|",blocks[6],"|",blocks[7],"|",blocks[8],"|")    

player1="x"
player2="o"

def rules(player):
    conditions=[
    [0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for check in conditions:
        if blocks[check[0]]==player and blocks[check[1]]==player and blocks[check[2]]==player:
            return 1
        return 0

def start_game():
    display_game()
    while True:
        while True:
            playeroption1=input(f"{player1}  Enter the place[1-9]:")
            if blocks[int(playeroption1) - 1] == "-":
                blocks[int(playeroption1) -1]=player1
                display_game()
                if rules(player1):
                    return f'Winner:{player1}'
                break
            else: 
                print("This place already alloted")

        while True:
            playeroption2=input(f"{player2}  Enter the place[1-9]:")
            if blocks[int(playeroption2) - 1] == "-":
                blocks[int(playeroption2) -1]=player2
                display_game()
                if rules(player1):
                    return f'Winner:{player1}'
                break
            else: 
                print("This place already alloted")


start_game()
