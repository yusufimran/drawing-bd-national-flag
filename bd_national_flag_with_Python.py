#Drawing National Flag of Bangladesh by Python Programming
# Written by Yusuf Imran

#pastebin link: https://pastebin.com/BFMSbm9d

import turtle as toru

#toru.speed(1)
toru.hideturtle()

def BD_NationalFlag(x,y,length):
  #1st step: Drawing the border, 10:6
  toru.begin_fill()
  toru.color("#01796F")

  length1=length*0.55; length2=length*0.60;
  length3=length*0.45;
  length4=length*0.10

  toru.penup(); toru.goto(x,y); toru.pendown()
  toru.goto(x+length1,y); toru.goto(x+length1,y+length2);
  toru.goto(x-length3,y+length2); toru.goto(x-length3,y); toru.goto(x,y)

  toru.end_fill()

  #2nd step: Drawing the circle of radius 20
  toru.penup()
  toru.goto(x,y+length4); #length4=length*0.10

  toru.pendown()

  toru.begin_fill()
  toru.color("#E11837");
  toru.circle(length*0.20)
  toru.end_fill()

length=300
BD_NationalFlag(0,0,length)

toru.exitonclick()
