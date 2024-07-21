S = input()
time = 0

for s in S:
    if s in "ABC":
        time += 3
    elif s in "DEF":
        time += 4
    elif s in "GHI":
        time += 5
    elif s in "JKL":
        time += 6
    elif s in "MNO":
        time += 7
    elif s in "PQRS":
        time += 8
    elif s in "TUV":
        time += 9
    elif s in "WXYZ":
        time += 10
    elif s in "":
        time += 2
    else:
        time += 11
        
print(time)