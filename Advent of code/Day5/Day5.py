with open("Advent of code\Day5\input.txt") as f:
    yes = f.read().splitlines()
    storage=[]
    for data in yes:
        lower1,upper1,lower2,upper2=0,127,0,7
        start1,start2=128,8
        var1,var2=0,0
        for i,info in enumerate(data):
            start1=int(start1/2)
            if info == "F":
                upper1-=start1
                # print("f: ",lower1,upper1)
                if i == 6:
                    # print(upper1)
                    var1=upper1
            if info == "B":
                lower1+=start1
                # print("b: ",lower1,upper1)
                if i == 6:
                    # print(lower1)
                    var1=lower1 


            if info == "R":
                start2=int(start2/2)
                lower2+=start2
                # print("R: ",lower2,upper2)
                if i == 9:
                    # print(upper2)
                    var2=upper2
            if info == "L":
                start2=int(start2/2)
                upper2-=start2
                # print("R: ",lower2,upper2)
                if i == 9:
                    # print(lower2)
                    var2=lower2
        jerry=(var1*8)+var2
        storage.append(jerry)
        storage.sort()
    print("answer1: ",max(storage))
    for i,x in enumerate(storage):
        i+=21
        if i not in storage:
            print("answer2: ",i)


