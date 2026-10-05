#print the first 4 lines of league
with open('league.txt','r') as file:
    for _ in range(4):
        line = file.readline()
        print(line, end='')