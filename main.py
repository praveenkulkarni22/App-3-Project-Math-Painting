from rectangle import Rectangle
from square import Square
from canvas import Canvas, FileSharer

canvas_width = int(input("Enter the Canvas Width: "))
canvas_height = int(input("Enter the Canvas Height: "))
canvas_color = input("Enter the Canvas Color: (Black or White): ")
colors = {'White': [255, 255, 255], 'Black': [0, 0, 0]}

canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])
while True:
    shape_type = input("Enter the Shape you want to draw. Enter Q to quit: ")
    if shape_type.lower() == "rectangle":
        rect_x = int(input("Enter x for Rectangle: "))
        rect_y = int(input("Enter y for Rectangle: "))
        rect_width = int(input("Enter width of Rectangle: "))
        rect_height = int(input("Enter height of Rectangle: "))
        rect_color_red = int(input("Enter the red value in RGB for Rectangle: "))
        rect_color_blue = int(input("Enter the blue value in RGB for Rectangle: "))
        rect_color_green = int(input("Enter the green value in RGB for Rectangle: "))
        rect = Rectangle(rect_x, rect_y, rect_width, rect_height, (rect_color_red, rect_color_blue, rect_color_green))
        rect.draw(canvas)
    elif shape_type.lower() == "square":
        sqr_x = int(input("Enter x for Square: "))
        sqr_y = int(input("Enter y for Square: "))
        sqr_side = int(input("Enter length of side of Square: "))
        sqr_color_red = int(input("Enter the red value in RGB for Square: "))
        sqr_color_blue = int(input("Enter the blue value in RGB for Square: "))
        sqr_color_green = int(input("Enter the green value in RGB for Square: "))
        square = Square(sqr_x, sqr_y, sqr_side, (sqr_color_red, sqr_color_blue, sqr_color_green))
        square.draw(canvas)
    elif shape_type.lower() == "q":
        break
canvas.make('canvas.png')

file_sharer = FileSharer(filepath = 'canvas.png')
print(file_sharer.share())
