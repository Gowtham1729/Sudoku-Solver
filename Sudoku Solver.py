from datetime import datetime
start=datetime.now()
f=open("puzzle.txt","r")
l=f.read()
lst=l.split("\n")
lst2=[1,2,3,4,5,6,7,8,9]+[]
lst5=[]
lst3=[]
d={}
d2={}
d4={}
lst7=[]
d5={}
for i in range(1,10):                                           #To create d1
    for j in range(1,10):
        d[(i,j)]=lst2+[]
c=1
for i in lst:                                                   #For d2
    k=1
    lst3=list(i)
    for j in lst3:
        try:
            if(int(j) in lst2):
                d2[(c,k)]=int(j)
                k=k+1
        except:
            None
            k=k+1
    c=c+1
c=0
b=81-len(d2)
while True:#Repeating many times
    for q in range(60):                                                           #Numbers row and colomn deleter
        d.update(d2)
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
    #########################################################################################################################
    lst10=[]
    for m in range(3):          ######Single prob in box value fixer
        for q in range(3):
            lst9=[1,2,3,4,5,6,7,8,9]
            for i in range(l1[m],l1[m+1]):
                for j in range(l1[q],l1[q+1]):
                    if((i,j) in d2):
                        value=d2[(i,j)]
                        for k in range(l1[m],l1[m+1]):
                            for l in range(l1[q],l1[q+1]):
                                if((k,l) in d2):
                                    try:
                                        lst9.remove(value)
                                    except:
                                        None
                    for f in lst9:
                        c=0
                        for k in range(l1[m],l1[m+1]):
                            for l in range(l1[q],l1[q+1]):
                                if((k,l) not in d2):
                                    if(f in d[(k,l)]):
                                        c=c+1
                                        s=(k,l)
                        if(c==1):
                            d2[s]=f
    
############################################Updater####################################
  
    for i in range(1,10):
            for j in range(1,10):
                if(type(d[(i,j)])==type([1])):
                   if(len(d[(i,j)])==1):
                        v=d[(i,j)][0]
                        d[(i,j)]=v
                        d4[(i,j)]=v
    d2.update(d4)
    n=0
    ##############################################################################################################################
    lst9=[1,2,3,4,5,6,7,8,9]
    for i in range(1,10):##############################Row single prob
        lst9=[1,2,3,4,5,6,7,8,9]
        for j in range(1,10):
            if((i,j) in d2):
                lst9.remove(d2[(i,j)])
        for k in lst9:
            c1=0
            c2=0
            for l in range(1,10):
                if((i,l) not in d2):
                    c=c+1
                    if(k in d[(i,l)]):
                        c2=c2+1
                        s=(i,l)
            if(c2==1):
                d2[(s)]=k
    for j in range(1,10):########################Colomn single prob
        lst9=[1,2,3,4,5,6,7,8,9]
        for i in range(1,10):
            if((i,j) in d2):
                lst9.remove(d2[(i,j)])
        for k in lst9:
            c1=0
            c2=0
            for l in range(1,10):
                if((l,j) not in d2):
                    c=c+1
                    if(k in d[(l,j)]):
                        c2=c2+1
                        s=(l,j)
            if(c2==1):
                d2[(s)]=k
    ###########################################################################################################################
    c=0
    
    for m in range(3):#############################################Row same box 2 elements common deleter
        for q in range(3):
            lst15=[1,2,3,4,5,6,7,8,9]+[]
            for i in range(l1[m],l1[m+1]):
                for j in range(l1[q],l1[q+1]):
                    if((i,j) in d2):
                        lst15.remove(d2[(i,j)])
            for k in lst15:
                lst2=[]
                for i in range(l1[m],l1[m+1]):
                    flag=0
                    for j in range(l1[q],l1[q+1]):
                        try:
                            if(k in d[(i,j)]):
                                c1=c1+1
                                flag=1
                                s=i
                        except:
                            None
                    lst2.append(flag)
                c2=0
                for i in lst2:
                    if(i==1):
                        c2=c2+1
                if(c2==1):
                    for i in range(1,10):
                        if(i not in range(l1[q],l1[q+1])):
                            try:
                                d[(s,i)].remove(k)
                            except:
                                None
            c=c+1
            
    #############################################colomn same box common elements deleter###################################################################################
    c=0
    for m in range(3):
        for q in range(3):
            lst15=[1,2,3,4,5,6,7,8,9]+[]
            for i in range(l1[m],l1[m+1]):
                for j in range(l1[q],l1[q+1]):
                    if((i,j) in d2):
                        lst15.remove(d2[(i,j)])
            for k in lst15:
                lst2=[]
                for i in range(l1[q],l1[q+1]):#Colomn
                    flag=0
                    for j in range(l1[m],l1[m+1]):#Row
                        try:
                            if(k in d[(j,i)]):
                                c1=c1+1
                                flag=1
                                s=i
                        except:
                            None
                    lst2.append(flag)
                c2=0
                for i in lst2:
                    if(i==1):
                        c2=c2+1
                if(c2==1):
                    for i in range(1,10):
                        if(i not in range(l1[m],l1[m+1])):
                            try:
                                d[(i,s)].remove(k)
                            except:
                                None
    ###############################################Two same elements in a row length 2 other deleter#########################################################################
    for i in range(1,10):
        for j in range(1,10):
            a=d[(i,j)]
            for k in range(1,10):
                b=d[(i,k)]
                if(a==b and j!=k and len(a)==2):
                    a1=b[0]
                    a2=b[1]
                    for u in range(1,10):
                        if(u!=k and u!=j):
                            y=d[(i,u)]
                            try:
                                y.remove(a1)
                            except:
                                None
                            try:
                                y.remove(a2)
                            except:
                                None
                            d[(i,u)]=y
    ##############################################Two same elements in a colomn length 2 other deleter#############3
    for i in range(1,10):
        for j in range(1,10):
            a=d[(j,i)]
            for k in range(1,10):
                b=d[(k,i)]
                if(a==b and j!=k and len(a)==2):
                    a1=b[0]
                    a2=b[1]
                    for u in range(1,10):
                        if(u!=k and u!=j):
                            y=d[(u,i)]
                            try:
                                y.remove(a1)
                            except:
                                None
                            try:
                                y.remove(a2)
                            except:
                                None
                            d[(u,i)]=y
    l1=[1,4,7,10]
    for m in range(3):#############################################SAme box 2 element deleter
        for q in range(3):
            for i in range(l1[m],l1[m+1]):
                for j in range(l1[q],l1[q+1]):
                    a=d[(i,j)]
                    for x in range(l1[m],l1[m+1]):
                        for y in range(l1[q],l1[q+1]):
                            b=d[(x,y)]
                            if(a==b):
                                if (not (i==x and j==y) and len(a)==2):
                                    for y1 in range(l1[m],l1[m+1]):
                                        for y2 in range(l1[q],l1[q+1]):
                                            if (not(y1==i and y2==j) and not(y1==x and y2==y)):
                                                a1=b[0]
                                                a2=b[1]
                                                try:
                                                    d[(y1,y2)].remove(a1)
                                                except:
                                                    None
                                                try:
                                                    d[(y1,y2)].remove(a2)
                                                except:
                                                    None
    '''
    lst=[]
    for i in range(1,10):
        for j in range(1,10):
            if((i,j) not in d2):
                if len(d[(i,j)])==2:
                    lst=lst+[d[(i,j)]]
        r=[]
        for p in range(len(lst)):
            for q in range(len(lst)):
                if p!=q:
                    t=lst[p]+lst[q]
                    for k in range(len(t)):
                        if t[k] not in r:
                            r.append(t[k])
                    for k in range(1,10):
                        if d[(i,k)]==r:
                            print 7
                            for x in r:
                                for m in range(1,10):
                                    if not(m==lst2[p] and m==lst2[q] and m==k):
                                        try:
                                            d[(i,m)].remove(x)
                                            print 6
                                        except:
                                            None
    '''

    if(len(d2)==81):
        break     
    f2=open("sampleoutput.txt","w")
    for i in range(1,10):
        for j in range(1,10):
            if(type(d[(i,j)])==type(1)):
                f2.write(str(d[(i,j)])+" ")
            else:
               f2.write("- ")
        f2.write("\n")
    f2.close()
    
    '''
    for i in range(1,10):
        lst=[]
        lst2=[]
        for j in range(1,10):
            if((i,j) not in d2):
                if len(d[(i,j)])==2:
                    lst=lst+[d[(i,j)]]
                    lst2=lst2+[j]
        r=[]
        for p in range(len(lst)):
            for q in range(len(lst)):
                if p!=q:
                    t=lst[p]+lst[q]
                    for k in range(len(t)):
                        if t[k] not in r:
                            r.append(t[k])
                    for k in range(1,10):
                        if d[(i,k)]==r:
                            print 7
                            for x in r:
                                for m in range(1,10):
                                    if not(m==lst2[q] and m==lst2[p] and m==k):
                                        try:
                                            d[(i,m)].remove(x)
                                            print (i,m),x
                                        except:
                                            None
    '''                                    
f2=open("puzzleoutput.txt","w")
for i in range(1,10):
    for j in range(1,10):
        if(type(d[(i,j)])==type(1)):
            f2.write(str(d2[(i,j)])+" ")
        else:
           f2.write("- ")
    f2.write("\n")
f2.close()
print datetime.now()-start
