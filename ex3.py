import turtle as tu

def draw_triangle(x,y,hdg,len):
    tu.up()
    tu.goto(x,y)
    tu.down()
    tu.setheading(hdg)
    tu.fd(len)
    tu.rt(360/3)
    tu.fd(len)
    tu.rt(360/3)
    tu.fd(len)
    return tu.position()

def draw_line(x,y,hdg,len):
    tu.up()
    tu.goto(x,y)
    tu.down()
    tu.setheading(hdg)
    tu.fd(len)
    return tu.position()

def draw_circle(x,y,hdg,len):
    for i in range(0,6):
        draw_triangle(x,y,hdg+((360/6)*i),len)
    return tu.position()

tu.speed(10000)

# clouds
tu.color('lightblue')
draw_circle(-230,150,0,30)
draw_circle(-160,110,0,30)
draw_circle(-100,170,0,30)
draw_circle(-50,120,0,30)
draw_circle(0,190,0,30)

#floor
tu.color('black')
tu.up()
tu.goto(-300,-240)
tu.down()
tu.goto(500,-240)


# tree
tu.color('brown')
tu.up()
tu.goto(200,-240)
tu.seth(90)
tu.down()
tu.fd(300)
branch1 = draw_line(200,-50,150,80)
branch2 = draw_line(200,-150,150,80)

tu.color('darkgreen')
draw_circle(200,150,30,100)
draw_circle(branch1[0],branch1[1],30,40)
draw_circle(branch2[0],branch2[1],30,40)


# cycle
## wheel
tu.color('yellow')
wheel1 = draw_circle(-200,-200,30,40)
tu.color('orange')
tu.up()
tu.goto(wheel1[0],wheel1[1])
tu.down()
tu.setheading(360/6)
tu.fd(80)
temp = tu.position()
tu.color('red')
tu.seth(45)
tu.fd(30)
tu.color('orange')
tu.up()
tu.goto(temp[0],temp[1])
tu.down()
draw_triangle(tu.position()[0],tu.position()[1],0,80)
tu.seth(0)
tu.fd(80)
draw_triangle(tu.position()[0],tu.position()[1],-60,80)
tu.color('red')
tu.setheading(30)
tu.fd(30)
tu.setheading(180)
tu.fd(30)


tu.color('yellow')
wheel2 = draw_circle(-40,-200,30,40)

tu.up()
tu.done()
