hi = input("hi? ")

def main():
    match hi.split():
        case ["cum", *args]:
            for i in args:
                print(i)
            
main()