f = open("text.txt")

tag = input("Intup tag ---> ")

p = False
for abz in f.read().split("\n\n"):
    if "#" + tag in abz:
        print(f"\n{abz}")
        p = True
if p == False:
    print("There is no such tag")