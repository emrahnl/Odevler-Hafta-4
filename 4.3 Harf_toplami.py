password=input("Pls enter a password: ")
total=0
for d in password:
    if d.isdigit():
        b=int(d)
        total=total+b
print(total)

            

