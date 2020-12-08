import re


with open("Advent of code\Day2\input.txt") as f:
    yes = f.read().splitlines()
    count1=0
    count2=0
    for data in yes:
        new = re.split("-|: | ",data)
        least,most,letter,string=new[0],new[1],new[2],new[3]
        if (int(string.count(letter)) >= int(least)) and (int(string.count(letter)) <= int(most)):
            count1 = count1+1
    print("answer1: ",count1)

    for data in yes:
        new = re.split("-|: | ",data)
        least,most,letter,string=new[0],new[1],new[2],new[3]
        if (string[int(least)-1] is letter) != (string[int(most)-1] is letter):
            count2=count2+1
    print("answer2: ",count2)