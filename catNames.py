catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to exit.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # concatenate list
print('The cat names are: ')
for name in catNames:
    print(' ' + name)
print('Enter a pet name: ')
name1 = input()
if name1 not in catNames:
    print('I do not have a pet named ' + name1)
else:
    print(name + ' is my pet.')
