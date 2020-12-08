
num=[]

with open("Advent of code\Day1\input.txt") as f:
    yes = f.read().splitlines()

    for read in yes:
        num.append(read)

    for i in range(len(num)):
        for j in range(len(num)):
            x=int(num[i])
            y=int(num[j])
            if x+y == 2020:
                print(x,y)
                print(x*y)
    print("break--------------------------------------------------------------------------------")
    for i in range(len(num)):
        for j in range(len(num)):
            for k in range(len(num)):
                x=int(num[i])
                y=int(num[j])
                z=int(num[k])
                if x+y+z == 2020:
                    print(x,y,z)
                    print(x*y*z)

