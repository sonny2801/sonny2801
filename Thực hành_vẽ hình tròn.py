import turtle
t = turtle.Turtle()
#Đặt kích thước cho viền hình tròn là 5
t.pensize(5)
#Đặt màu sắc cho viền hình tròn là màu xanh
t.pencolor("blue")
#Tùy chỉnh điểm bắt đầu vẽ hình tròn
t.goto(-40,120)
#Đặt màu nền cho hình tròn là màu đỏ
t.fillcolor("red")
t.begin_fill()
#Đặt bán kính của hình tròn là 150
t.circle(150)
t.end_fill()
turtle.done()