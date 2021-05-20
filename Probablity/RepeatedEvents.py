import math
try:
    a = float(input("Percent chance of Event: "))
    b = int(input("Number Of times occured: "))
except Exception as e:
    print(e)


def calc(event,occur):
    return round(math.pow(event*0.01,occur)*100,6)


print(calc(a,b))