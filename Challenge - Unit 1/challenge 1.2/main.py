# leap year tester

def isleap(year):
    if not(year % 400):
        return 1
    elif not(year % 100) :
        return 0
    elif not(year % 4):
        return 1

    return 0

if __name__ == "__main__" :
    y = int(input("Enter year to test : "))
    print("{} is {} leap year".format(y, 'a' if isleap(y) else 'not a' ))

