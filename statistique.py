import random
import turtle

tit = turtle.Turtle()
tit.penup()
tit.ht()
tit.goto(-150,250)
tit.write('expérience de Stern et Gerlach',font=('Arial', 20, 'normal'))

turtle.title('expérience de Stern et Gerlach')

ecrant = turtle.Turtle()
ecrant.ht()
ecrant.penup()
ecrant.goto(175,200)
ecrant.pendown()
ecrant.goto(175,-200)

e = turtle.Turtle()
e.ht()
e.penup()
e.goto(178,210)
e.write('[E]',font=('Arial', 25, 'normal'))

m_up = turtle.Turtle()
m_up.speed(10)
m_up.ht()
m_up.penup()
m_up.goto(-30,100)
m_up.pendown()
m_up.pencolor('blue')
m_up.fd(25)
m_up.lt(-90)
m_up.fd(50)
m_up.lt(-90)
m_up.fd(25)
m_up.lt(-90)
m_up.fd(50)

n = turtle.Turtle()
n.pencolor('blue')
n.speed(10)
n.ht()
n.penup()
n.goto(-23,65)
n.write('N',font=('Arial', 15, 'normal'))


m_down = turtle.Turtle()
m_down.speed(10)
m_down.ht()
m_down.penup()
m_down.goto(-30,-50)
m_down.pendown()
m_down.pencolor('red')
m_down.fd(25)
m_down.lt(-90)
m_down.fd(50)
m_down.lt(-90)
m_down.fd(25)
m_down.lt(-90)
m_down.fd(50)

s = turtle.Turtle()
s.pencolor('red')
s.speed(10)
s.ht()
s.penup()
s.goto(-23,-82)
s.write('S',font=('Arial', 15, 'normal'))


surce = turtle.Turtle()
surce.shape('circle')
#surce.ht()
surce.penup()
surce.goto(-270,0)
surce.pendown()


elec = turtle.Turtle()
elec.ht()
elec.penup()
elec.goto(-290,20)
elec.write('electrons(e-)',font=('Arial', 10, 'normal'))


p = turtle.Turtle()
p.ht()
p.penup()
p.goto(178,108)
p.write('| ↑ > :',font=('Arial', 20, 'normal'))

n = turtle.Turtle()
n.ht()
n.penup()
n.goto(178,-108)
n.write('| ↓ > :',font=('Arial', 20, 'normal'))


pp=0
pn=0

while(True):
    up = turtle.Turtle()
    up.ht()
    up.penup()
    up.goto(240,108)
    up.write('  {}'.format(pp),font=('Arial', 20, 'normal'))

    down = turtle.Turtle()
    down.ht()
    down.penup()
    down.goto(240,-108)
    down.write('  {}'.format(pn),font=('Arial', 20, 'normal'))
    
    pb = random.randint(0,20)
    
    if (pb<10):
        e_up = turtle.Turtle()
        e_up.speed(3)
        e_up.turtlesize(0.5)
        e_up.penup()
        e_up.goto(-265,0)
        e_up.color('blue')
        e_up.shape('circle')
        #e_up.pendown()
        e_up.goto(-30,0)
        e_up.goto(170,random.randint(95,115))
        pp=pp+1
        
    elif (pb>10):
        e_down = turtle.Turtle()
        e_down.speed(3)
        e_down.turtlesize(0.5)
        e_down.penup()
        e_down.goto(-265,0)
        e_down.color('red')
        e_down.shape('circle')
        #e_down.pendown()
        e_down.goto(-30,0)
        e_down.goto(170,- random.randint(95,115))
        pn=pn+1


    up.clear()
    down.clear()
