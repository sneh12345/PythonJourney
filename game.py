from turtle import *
color('blue', 'yellow')
begin_fill()
while True:
    forward(203210)
    left(1)
    if abs(pos()) < 1321:
        break
end_fill()
done()

