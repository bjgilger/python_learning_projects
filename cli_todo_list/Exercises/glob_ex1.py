import glob

myfiles = glob.glob("Exercises/files/*.txt")
# print(myfiles)
for filepath in myfiles:
    with open(filepath, "r") as f:
        print(f.read())
