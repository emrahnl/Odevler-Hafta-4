file = open("futbolcular.txt", "r")

new_file=open("eng_futbolcular.txt","a+")

for line in file:
    line=line.replace("ı","i")
    line=line.replace("ü","u")
    line=line.replace("ö","o")
    line=line.replace("ç","c")
    line=line.replace("ş","s")
    line=line.replace("ğ","g")
    line=line.replace("İ","i")
    line=line.replace("Ü","u")
    line=line.replace("Ö","O")
    line=line.replace("Ç","c")
    line=line.replace("Ş","S")
    

    new_file.write(line)
    print(line)
    
new_file.close()
