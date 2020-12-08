with open("Advent of code\Day3\input.txt") as f:
        yes = f.read().splitlines()
        count1=0
        tempstore=[]
        for data in yes:
            value = data*(count1+1)
            tempstore.append(value)
            count1+=1

        count1=0
        count2=0
        for i in range(len(tempstore)):
            if tempstore[i][count1*3] == "#":
                count2+=1
            count1+=1
        print("answer1: ", count2)

        count1=0
        c1,c2,c3,c4,c5=0,0,0,0,0
        for i in range(len(tempstore)):
            if tempstore[i][count1*1] == "#":
                c1+=1
            if tempstore[i][count1*3] == "#":
                c2+=1
            if tempstore[i][count1*5] == "#":
                c3+=1
            if tempstore[i][count1*7] == "#":
                c4+=1
            if i%2 == 0:
                if tempstore[i][int(count1/2)] == "#":
                    c5+=1
            count1+=1
        print("answer2: ", c1*c2*c3*c4*c5)

