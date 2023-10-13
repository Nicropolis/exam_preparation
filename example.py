import turtle as t
t.hideturtle()
k = 100
t.color("black","red")
t.speed(0)
t.begin_fill()
t.seth(90)
t.right(90)
for i in range(4):
    t.forward(4 * 5 ** 0.5 * k)
    t.right(150)
    t.forward(4 * 5 ** 0.5 * k)
    t.right(300)
t.end_fill()
cv = t.getcanvas()
otv = [1 if (h:=cv.find_overlapping(x,y,x,y)) and (cv.itemcget(h[-1],"fill") == "red") else 0
for x in range(-200 * k,200 * k, k) for y in range(-200 * k,200 * k, k)]
print(otv.count(1))
t.done()
