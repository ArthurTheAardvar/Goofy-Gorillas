

cases = int(input()) 

for i in range(cases): #go through the other lines
    line = input()
    
    line = line.split(" ") #split up the line by spaces
    line[0] = str(line[0])
    line[1] = str(line[1])
    if line[0] == "true" and line[1] == "true":
        print("true")
    elif line[0] == "true" and line[1] == "false":
        print("false")
    elif line[0] == "false" and line[1] == "true":
        print("false")
    elif line[0] == "false" and line[1] == "false":
        print("true")




   
