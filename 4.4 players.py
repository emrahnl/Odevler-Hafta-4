players=[]
with open("futbolcular.txt", "r") as file:
    for line in file:
        player=line.split(",")
        if player[0].startswith("A"):
            players.append(player)
        if player[0].startswith("E"):
            players.append(player)
        if player[0].startswith("U"):
            players.append(player)
        if player[0].startswith("I"):
             players.append(player)
        if player[0].startswith("O"):
             players.append(player)

with open("yeni_futbolcular.txt","w") as file:
    for player in players:
        file.write(",".join(player))
    




            
    
