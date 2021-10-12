

import math
import turtle
t=turtle.Turtle()
screen=turtle.Screen()

t.speed(0.01)


#initializing the radius of the bigger circle
radius=200     


# function to draw the target                               
def concentricCircle(radius, colors):
    
    
    if len(colors)==0:
     
        t.pencolor("black")
        return 'Done'
    
    else:
        width = radius/len(colors)
        turtle.title('Drawing of Achery Target')
        turtle.bgcolor('Pink')
        
        t.pencolor(colors[0])
        
        color=colors[0]
        t.fillcolor(color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        colors.pop(0)
        t.setposition(t.xcor(), t.ycor()+width)
        concentricCircle(radius-width, colors)
    
Target=concentricCircle(200,colors=(['white','black','blue', 'red','yellow']))



num_clicks=0
total_score=0


# callback function
def mouse_clicks(xpos, ypos):
    global total_score ,num_clicks
    list1=[xpos, ypos]
    # print(list1)
    width = radius/5

    click_distance = math.sqrt((xpos - t.xcor())**2 + (ypos - t.ycor())**2 )
    if width*4< click_distance< width * 5:
        total_score+=1
        print("You hit white and scored 1 pts")
    
    elif width*3<click_distance<=width*4:
        total_score += 3
        print("You hit black and scored 3 pts")

    elif width*2<click_distance<=width*3:
        total_score += 5
        print("You hit blue and scored 5 pts") 
        
        
    elif width<click_distance<=width*2:
        total_score += 7
        print("You hit red and scored 7 pts")  
        
    elif click_distance< width:
        total_score += 9
        print("You hit bulls-eye(yellow) and scored 9 pts")
        
    elif click_distance > width*5:
        total_score += 0
        print("You missed all the targets, Try again") 

    
    num_clicks += 1
    if num_clicks ==5:
        t.screen.onclick(None)
        print("you are have exhausted all your chances")
        print(f"Your total score is {total_score}")
        
        
# def test():
#     test1=mouse_clicks(70,65)
#     test2=mouse_clicks(-100,65)
#     test3=mouse_clicks(30,85)
# test()
 
t.screen.onclick(mouse_clicks,1)
turtle.done()






