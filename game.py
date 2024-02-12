block=["-" for i in range(9)]

player1="x"
player2="0"

def display():
    print("|",block[0],"|",block[1],"|",block[2],"|")
    print("|",block[3],"|",block[4],"|",block[5],"|")
    print("|",block[6],"|",block[7],"|",block[8],"|")

def rules(player):
    conditions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for check in conditions:
        if 

display()