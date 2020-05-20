print("enter number")
number = input()


def collatz(number):
    mod = int(number) % 2
    if mod == 0:
        newone = int(number) // 2
        print(str(newone))
    else:
        newtwo = 3 * int(number) + 1
        print(str(newtwo))

collatz(number)