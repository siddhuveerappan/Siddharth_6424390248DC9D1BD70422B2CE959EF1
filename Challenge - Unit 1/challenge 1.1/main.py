#recursive factorial

def factorial(n):
    if n <= 0:
        return 1

    return n * factorial(n-1)

if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print("{}! = {}".format(num, factorial(num)))
