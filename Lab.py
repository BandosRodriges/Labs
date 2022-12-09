f = open("text.txt")

word = input("Intup your word:")

r = False
for lines in f.read().split("\n\n"):
    if word in lines:
        print(f"\n{lines}")
        r = True
if r == False:
    print("There is no such word!")