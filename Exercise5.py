# Health Management system
def getdate():
    import datetime
    return datetime.datetime.now()

def log(n):
    if n == 1:
        n1 = int(input("Press\n 1 for exercise\n 2 for food\n"))
        if n1 == 1:
            n2 = input("Type here\n")
            with open("harry_e.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + n2 + "\n")
                print("Successfully written\n")
        elif n1 == 2:
            n2 = input("Type here\n")
            with open("harry_f.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + n2 + "\n")
                print("Successfully written\n")
    elif n == 2:
        n1 = int(input("Press\n 1 for exercise\n 2 for food\n"))
        if n1 == 1:
            n2 = input("Type here\n")
            with open("rohan_e.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + n2 + "\n")
                print("Successfully written\n")
        elif n1 == 2:
            n2 = input("Type here\n")
            with open("rohan_f.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + n2 + "\n")
                print("Successfully written\n")
    elif n == 3:
        n1 = int(input("Press\n 1 for exercise\n 2 for food\n"))
        if n1 == 1:
            n2 = input("Type here\n")
            with open("hammad_e.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + n2 + "\n")
                print("Successfully written\n")
        elif n1 == 2:
            n2 = input("Type here\n")
            with open("hammad_f.txt","a") as f:
                f.write(str([str(getdate())]) + ": " + n2 + "\n")
                print("Successfully written\n")
    else:
        print("enter Valid number 1 ,2 or 3\n")

def retrieve(n):
    if n == 1:
        n1 = int(input("press\n 1 for exercise\n 2 for food\n"))
        if n1 == 1:
            with open("harry_e.txt") as f:
                for i in f:
                    print(i,end="")
        elif n1 == 2:
            with open("harry_f.txt") as f:
                for i in f:
                    print(i,end="")
    elif n == 2:
        n1 = int(input("press\n 1 for exercise\n 2 for food\n"))
        if n1 == 1:
            with open("rohan_e.txt") as f:
                for i in f:
                    print(i, end="")
        elif n1 == 2:
            with open("rohan_f.txt") as f:
                for i in f:
                    print(i, end="")
    elif n == 3:
        n1 = int(input("press\n 1 for exercise\n 2 for food\n"))
        if n1 == 1:
            with open("hammad_e.txt") as f:
                for i in f:
                    print(i, end="")
        elif n1 == 2:
            with open("hammad_f.txt") as f:
                for i in f:
                    print(i, end="")


    else:
        print("Enter valid number\n")


a = int(input("Press\n 1 for log\n 2 for retrieve\n"))
if a == 1:
    b = int(input("Press\n 1 for harry\n 2 for rohan\n 3 for hammad\n"))
    log(b)
else:
    b =  int(input("Press\n 1 for harry\n 2 for rohan\n 3 for hammad\n"))
    retrieve(b)

















