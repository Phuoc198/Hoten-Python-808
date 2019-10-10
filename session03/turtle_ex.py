from turtle import *
speed(-1)
shape("turtle")
#color("red")

items = ['red','blue','green','yellow','pink','gray']

for i,item in enumerate(items):
    color(items[i])
    forward(100)
    left(60)
    

# for i in range(4):

#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)

#     right(10)



mainloop()