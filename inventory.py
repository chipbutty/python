stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }

def displayInventory(inventory):
    print("inventory:")
    item_total = 0
    for k, v in inventory.items():
        print (k, v)
        item_total = item_total + v
    print("total number of items: " + str(item_total))

displayInventory(stuff)
print ('\n')
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, loot):
    for i in loot:
        #print (i)
        if i not in inventory.keys() :
            inventory.update({i : 1})
        else:
            inventory.update({i : inventory[i]+1})
    #print (inventory.items())

inv = addToInventory(stuff, dragonLoot)

displayInventory(stuff)