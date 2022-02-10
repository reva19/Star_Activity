
import turtle
turtle.hideturtle()
turtle.speed(2)
turtle.fillcolor("orange")


def draw_star(dist,angle):
    for i in range(5): 
        turtle.forward(dist)
        turtle.right(angle)

for j in range(0,3):
    turtle.begin_fill()
    draw_star(100,144) 
    turtle.end_fill() 
    
    
    turtle.penup()
    turtle.setpos(-100,1)
    turtle.pendown()
    turtle.begin_fill()
    draw_star(75,144) 
    turtle.end_fill() 
    
    
    turtle.penup()
    turtle.setpos(-180,1)
    turtle.pendown()
    turtle.begin_fill()
    draw_star(50,144) 
    turtle.end_fill() 
    break

    
    

