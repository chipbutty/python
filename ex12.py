#"List Ends - ex.12"
list = [0,1,2,3,4,5,6,7]

def endList(alist):
   return[alist[0],alist[len(alist)-1]]

ends = endList(list)
print(ends)
