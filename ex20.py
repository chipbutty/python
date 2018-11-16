#"Element Search - ex.20"
import random

list = []
list = random.sample(range(100), 25)
list.sort()

b = random.randint(1, 100)

def BinarySearch(l, elem):
    sIndex = 0
    eIndex = len(l) - 1

    while True:
        mIndex = int((eIndex - sIndex) / 2)

        if mIndex < sIndex or mIndex > eIndex or mIndex < 0:
            return False
        mElement = l[mIndex]

        if (mElement == elem):
            return True
        elif (mElement < elem):
            sIndex = mIndex
        else:
            eIndex = mIndex

print(list, b)
result = BinarySearch(list, b)
print(result)