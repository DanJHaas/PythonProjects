#passports must have all criteria except cid which is optional
import re

with open("Advent of code\Day4\input.txt") as f:
    yes = f.read().splitlines()
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    color = ["amb","blu","brn","gry","grn","hzl","oth"]
    fieldscorrect=[]
    passport=0
    ck=0
    correct=0
    correct2=-1
    hot = []
    dictdata={}
    d1,d2,d3,d4,d5,d6,d7=False,False,False,False,False,False,False
    f=0
    for data in yes:
        f+=1
        if not data == "":
            t1=re.split("\n| ",data)
            hot=hot+t1
            for check in fields:
                if check in data:
                    fieldscorrect.append(check)
                    ck+=1



        if (data == "") or (f == 1102): 
            if (ck == 8) or ((ck == 7) and ("cid" not in fieldscorrect)):
                correct+=1
                for i in hot:
                    c=re.split(":",i)
                    dictdata[c[0]]=c[1]
                # print(dictdata)
                for info in fields:
                    try:
                        x = dictdata[info]
                        if info == "byr":
                            d1=(len(x) == 4) and (int(x)>=1920 and int(x)<=2002)
                        if info == "iyr":
                            d2=(len(x) == 4) and (int(x)>=2010 and int(x)<=2020)
                        if info == "eyr":
                            d3=(len(x) == 4) and (int(x)>=2020 and int(x)<=2030)
                        if info == "hgt":
                            if "in" in x:
                                x=(int(str(x).replace("in","")))
                                d4=(int(x)>=59 and int(x)<=76)
                            elif "cm" in x:
                                x=(int(str(x).replace("cm","")))
                                d4=(int(x)>=150 and int(x)<=193)
                        if info == "hcl":
                            d5=re.match(r"^#[a-f0-9]{6}",x)
                        if info == "ecl":
                            d6=(x in color)
                        if info == "pid":
                            d7 = re.match(r"[0-9]{9}",x)

                    except:
                        None
                        # print("not ",info)
                if ((d1 and d2) and (d3 and d4)) and ((d5 and d6) and d7):
                    # print("valid")
                    correct2+=1
                d1,d2,d3,d4,d5,d6,d7=False,False,False,False,False,False,False
            else:
                None
            # print("------------------------------------------------------------------"+"passport: ",passport,"CK: "+str(ck)+" ^^^")
            ck=0
            passport+=1
            fieldscorrect=[]
                
    print("answer1: ",correct)
    print("answer2: ",correct2)

