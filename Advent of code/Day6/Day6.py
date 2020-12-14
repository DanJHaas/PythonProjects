with open("Advent of code\Day6\input.txt") as f:
    txtfile = f.read().splitlines()
    storage=[]
    storage2=[]
    answer1=0
    answer2=0
    temp=0
    for word in txtfile:
        if not word == "": 

            for letter in word:
                storage2.append(letter)
                if letter not in storage:
                    storage.append(letter)

            temp+=1
        else:
            answer1+=len(storage)

            for letter in storage:
                if temp == storage2.count(letter):
                    answer2+=1

            temp=0
            storage=[]
            storage2=[]
    print(answer1)
    print(answer2)