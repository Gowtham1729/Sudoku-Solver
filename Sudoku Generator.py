def checker(d):
    d2={}
    d4={}
    for i in range(1,10):
        for j in range(1,10):
            if(d[(i,j)]!="-"):
                d2[(i,j)]=d[(i,j)]+0
            else:
                d[(i,j)]=range(1,10)+[]
    d.update(d2)
    for u1 in range(10):
        for i in range(1,10):
            for j in range(1,10):
                if((i,j) in d2):
                    v=d2[(i,j)]
                    for k in range(1,10):
                        if(k!=j):
                            try:
                                y=d[(i,k)]
                                y.remove(v)
                                d[(i,k)]=y
                            except:
                                None
                    for l in range(1,10):
                        if(l!=i):
                            try:
                                y=d[(l,j)]
                                y.remove(v)
                                d[(l,j)]=y
                            except:
                                None
        d.update(d2)
        for i in range(1,10):############################Value extracter
            for j in range(1,10):
                if(type(d[(i,j)])==type([1])):
                   if(len(d[(i,j)])==1):
                        v=d[(i,j)][0]
                        d[(i,j)]=v
                        d4[(i,j)]=v
        d2.update(d4)
        l1=[1,4,7,10]
        l2=[1,4,7,10]
        for m in range(3):                                      ####Box elements deleter
            for q in range(3):
                for i in range(l1[m],l1[m+1]):
                    for j in range(l1[q],l1[q+1]):
                        if((i,j) in d2):
                            value=d2[(i,j)]
                            for k in range(l1[m],l1[m+1]):
                                for l in range(l1[q],l1[q+1]):
                                    if((k,l) not in d2):
                                        try:
                                            v=d[(k,l)]
                                            v.remove(value)
                                            d[(k,l)]=v
                                        except:
                                            None
        flag=0
        for i in range(1,10):
            for j in range(1,10):
                try:
                    if(len(d[(i,j)]==0)):
                       return 1
                except:
                    None
    return flag

import random
a=random.randint(0,9)
f=open("sudoku questions/text"+str(a)+".txt","r")
l=f.read()
lst=l.split("\n")
c=1
d2={}
d6={}
d={}
lst2=[1,2,3,4,5,6,7,8,9]
for i in lst:                                                   #For d2
    k=1
    lst3=list(i)
    for j in lst3:
            if(int(j) in lst2):
                d2[(c,k)]=int(j)
            k=k+1
    c=c+1
lst2=[]
for i in range(1,10):
    lst=[]
    for j in range(1,10):
        lst.append(d2[(i,j)])
    lst2.append(lst)
k=[[0,1,2],[3,4,5],[6,7,8]]
i=0
for u in range(20):
    i=0
    while(i<3):
        a=random.choice(k[i])
        y=k[i]+[]
        y.remove(a)
        b=random.choice(y)
        lst2[a],lst2[b]=lst2[b],lst2[a]
        k=[[0,1,2],[3,4,5],[6,7,8]]
        i=i+1
        k=[[0,1,2],[3,4,5],[6,7,8]]
    j=0
    while(j<3):
        a=random.choice(k[j])
        y=k[j]+[]
        y.remove(a)
        b=random.choice(y)
        for y1 in range(0,9):
            lst2[y1][a],lst2[y1][b]=lst2[y1][b],lst2[y1][a]
        j=j+1
        k=[[0,1,2],[3,4,5],[6,7,8]]
    a1=random.randint(1,9)
    b1=range(1,10)+[]
    b1.remove(a1)
    b1=random.choice(b1)
    for i in range(0,9):
        for j in range(0,9):
            if(lst2[i][j]==a1):
                s1=j
            if(lst2[i][j]==b1):
                s2=j
        lst2[i][s1],lst2[i][s2]=lst2[i][s2],lst2[i][s1]
f2=open("answer.txt","w")
for i in range(0,9):
    for j in range(0,9):
        f2.write(str(lst2[i][j])+"  ")
    f2.write("\n")
f2.close()
d={}
d6={}
for i in range(1,10):
    for j in range(1,10):
        d[(i,j)]=lst2[i-1][j-1]
        d6[(i,j)]=lst2[i-1][j-1]
c=0
for i in range(1,10):
    while(c<16):
        a=range(1,10)
        i1=random.choice(a)
        d[(i,i1)]="-"
        d[(i1,i)]="-"
        d6[(i,i1)]="-"
        d6[(i1,i)]="-"
        a=checker(d)
        if(a==0):
            c=c+1
        c=c%8
        if(c%2==0):
            break
f3=open("puzzle.txt","w")
for i in range(1,10):
    for j in range(1,9+1):
        f3.write(str(d6[(i,j)]))
    f3.write("\n")
f3.close()

             
    
        













        
