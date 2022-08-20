class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        # The canvas is already drawn in the canvas class.
        # Now, we only change the color of the specific range.
        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.color

