def readnotes():
    ja=float(input("Write a note for a student"))
    return ja

def result(ja1,ja2):
    average = (ja1+ja2)/2
    print("Note 1: ",ja1)
    print("note 2: ",ja2)
    print("average: ",average, "Result: ",end="")
    if average >= 6.5:
        print("Nice, you IN")
    else:
        print("you are declined kkkk")

    
a = readnotes()
b = readnotes()
result(a,b)