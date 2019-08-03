import random


def guessing(n):
    m = int(input())
    if (m == n):
        print("Congratulation!You got it!")
        print("Let's play again!")
        main()
        # question()
    if (m > n):
        print("Sorry it is too high.")
        ask(n)
    else:
        print("Sorry it is too low.")
        ask(n)


def question():
    print("Wanna play again?")
    f = input("[Y/N]\n")
    if f is 'Y':
        main()
    elif f is 'N':
        print("Byebye!")
    else:
        print("error>_<")


def ask(n):
    print("Please try again!")
    guessing(n)


def main():
    print("Please input the number you guess between 1 & 100")
    a = random.randint(1, 100)
    guessing(a)


main()
