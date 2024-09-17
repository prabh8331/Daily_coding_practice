mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

lx= len(mat)
ly= len(mat[0])
total_itr = lx*ly

sy = 0
sx = 0

i = 0
lst=[]
dif = 0
keep_going = True

while keep_going:
    y=dif
    x=dif
    for y in range(y,ly-dif):
        print(x,y)
        i +=1

    if i >= total_itr:
        break

    for x in range(x+1,lx-dif):
        print(x,y)
        i +=1

    if i >= total_itr:
        break

    for y in list(reversed(range(sy+dif,y))):
        print(x,y)
        i +=1
    
    if i >= total_itr:
        break

    dif +=1 

    for x in list(reversed(range(sx+dif,x))):
        print(x,y)
        i +=1
        
    if i >= total_itr:
        break
    
