allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 2, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1},
             'Tim': {'ham sandwiches': 2, 'pretzels':12, 'cups': 2}
             }

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things brought:')
print(' - Apples            ' + str(totalBrought(allGuests, 'apples')))
print(' - Pretzels          ' + str(totalBrought(allGuests, 'pretzels')))
print(' - Ham Sandwiches    ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Cups              ' + str(totalBrought(allGuests, 'cups')))
print(' - Apple Pies        ' + str(totalBrought(allGuests, 'apple pies')))

