import turtle
d3={}
d4={}
t=turtle.Turtle()
t.pu()
t.goto(-180,180)
t.pd
t.speed(0)
for i in range(10):
    t.pd()
    t.fd(360)
    t.pu()
    t.bk(360)
    t.rt(90)
    t.fd(40)
    t.lt(90)
t.pu()
t.goto(-180,180)
t.rt(90)
for i in range(10):
    t.pd()
    t.fd(360)
    t.pu()
    t.bk(360)
    t.lt(90)
    t.fd(40)
    t.rt(90)
f=open("puzzle.txt","r")
l=f.read()
lst=l.split("\n")
c=1
d2={}
lst2=[1,2,3,4,5,6,7,8,9]
for i in lst:                                                   #For d2
    k=1
    lst3=list(i)
    for j in lst3:
        try:
            if(int(j) in lst2):
                d2[(c,k)]=int(j)
                d3[(c,k)]=int(j)
                k=k+1
        except:
            None
            k=k+1
    c=c+1
c1=-180
c2=180
d={}
for i in range(9):
    c1=-160
    for j in range(9):
        d[(i+1,j+1)]=(c1,c2)
        c1=c1+40
    c2=c2-40
for i in range(1,10):
    for j in range(1,10):
        if((i,j) in d2):
            t.pu()
            a=d[(i,j)]
            t.goto(a[0],a[1]-40)
            t.pencolor("blue")
            t.write((str(d2[(i,j)])),align="center", font=("Arial", 25, "normal"))
            t.pd()
t.ht()
t.pencolor("black")
while True:
    r=input("Enter the row number:")
    c=input("Enter the colomn number:")
    r=int(r)
    c=int(c)
    if((r,c) not in d3):
        if((r,c) not in d2):
            v=input("Enter the value to be entered in"+str((r,c))+"'s place:")
            v=int(v)
            d2[(r,c)]=v
            t.pu()
            a=d[(r,c)]
            t.goto(a[0],a[1]-40)
            t.write((str(d2[(r,c)])),align="center", font=("Arial", 25, "normal"))
            t.pd()
        else:
            t.pu()
            t.pu()
            a=d[(r,c)]
            t.goto(a[0]-19,a[1]-19-1)
            t.pd()
            t.color("white")
            t.begin_fill()
            t.circle(19)
            t.end_fill()
            t.pu()
            t.color("black")
            v=input("Enter the value to be entered in"+str((r,c))+"'s place:")
            v=int(v)
            d2[(r,c)]=v
            t.pu()
            a=d[(r,c)]
            t.goto(a[0],a[1]-40)
            t.write((str(d2[(r,c)])),align="center", font=("Arial", 25, "normal"))
            t.pd()
    else:
        print ("Sorry..YOu cant modify given values")
    if(len(d2)==81):
        print ("You entered all the values")
        break
    print ("*******************")
f3=open("puzzleoutput.txt","r")
lst2=[1,2,3,4,5,6,7,8,9]
d5={}
for i in lst:                                                   #For d2
    k=1
    lst3=list(i)
    for j in lst3:
        try:
            if(int(j) in lst2):
                d5[(c,k)]=int(j)
                k=k+1
        except:
            None
            k=k+1
    c=c+1
c=0
if(d5==d2):
    print ("Your answer is correct")
else:
    print ("Your answer is wrong")















        
