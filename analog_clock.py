from graphics import Canvas
import math
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
x0 = CANVAS_WIDTH / 2 
y0 = CANVAS_HEIGHT / 2
left_x = x0 -150
top_y  = y0 -150 
right_x = x0+150
bottom_y = y0+150
radius = 150
DELAY = 0.96

def main():
    draw_clock()
    line1 = canvas.create_line(200, 50, 200, 200, 'white')
    line2 = canvas.create_line(200, 200, 350, 200, 'white')
    line3 = canvas.create_line(200, 200, 200, 350, 'white')
    line4 = canvas.create_line(50, 200, 200, 200, 'white')
    line5 = canvas.create_line(200, 50, 200, 200, 'red')
    line6 = canvas.create_line(200, 70, 200, 200, 'blue')
    line7 = canvas.create_line(200, 90, 200, 200, 'green')
    #oval2 = canvas.create_oval(195, 45, 205, 55, 'red')
    #oval3 = canvas.create_oval(195, 65, 205, 75, 'green')
    #oval4 = canvas.create_oval(195, 85, 205, 95, 'black')
    step_size = 0.105; step_size2 = 0.5236
    count = 0; count2 = 0; count3 = 0
    th = (math.pi)*(3/2) ; th2 = (math.pi)*(3/2); th3 = (math.pi)*(3/2)
    while True:
        count = 0; th = (math.pi)*3/2
        while th < ((math.pi)*(3/2)+(2 * math.pi)):
            X1 = x0 + math.cos(th)*radius;
            Y1 = y0 + math.sin(th)*radius;
            canvas.delete(line5)
            line5 = canvas.create_line(x0, y0, X1, Y1, 'red')
            count += 1
            print(count)
            #canvas.moveto(oval2, X1, Y1)
            th += step_size
            time.sleep(DELAY)
        if count>=60:
            X2 = x0 + math.cos(th2)*(radius-20);
            Y2 = y0 + math.sin(th2)*(radius-20);
            canvas.delete(line6)
            line6 = canvas.create_line(x0, y0, X2, Y2, 'blue')
            count2 += 1
            print("y2 = ",count2, X2, Y2)
            #canvas.moveto(oval3, X2, Y2)
            th2 += step_size
        if count2>=60:
            #count2 += 0
            th2 = 0
            X3 = x0 + math.cos(th3)*(radius-40);
            Y3 = y0 + math.sin(th3)*(radius-40);
            canvas.delete(line7)
            line7 = canvas.create_line(x0, y0, X3, Y3, 'green')
            #canvas.moveto(oval4, X3, Y3)
            count3 += 1
            print(count3)
            th3 += step_size2
        if count3>12:
            count = 0; count2 = 0; count3 = 0
            th = 0; th2 = 0; th3 = 0
            
            
def draw_clock():

    oval1 = canvas.create_oval(left_x, top_y, right_x, bottom_y, 'tan')
    oval1 = canvas.create_oval(left_x+20, top_y+20, right_x-20, bottom_y-20, 'gray')
    oval1 = canvas.create_oval(left_x+40, top_y+40, right_x-40, bottom_y-40, 'white')
    step_size = 0.105; step_size2 = 0.523
    th1 = 0; th2 = 0
    while th1 < 2 * math.pi:
        XS = x0 + math.cos(th1)*radius;
        YS = y0 + math.sin(th1)*radius;
        oval5 = canvas.create_oval(XS-2, YS-2, XS+4, YS+4, 'white')
        th1 += step_size
    while th2 < 2 * math.pi:
        XM = x0 + math.cos(th2)*(radius-20);
        YM = y0 + math.sin(th2)*(radius-20);
        XH = x0 + math.cos(th2)*(radius-40);
        YH = y0 + math.sin(th2)*(radius-40);
        oval5 = canvas.create_oval(XM-2, YM-1, XM+2, YM+1, 'blue')
        oval5 = canvas.create_oval(XH-2, YH-1, XH+2, YH+1, 'black')
        th2 += step_size2
if __name__ == "__main__":
    main()