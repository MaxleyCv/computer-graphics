import math
import tkinter as tk

WINDOW_TITLE = "Lab #2"
WINDOW_WIDTH = 800
WINDOW_LENGTH = 800
WINDOW_GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_LENGTH}"
TABULATIONS_PER_AXIS = 5
ZERO_X, ZERO_Y = 400, 400

# Drawing constants
CIRCLE_RADIUS = 150
LINE_LENGTH = 200
ARROW_THRESHOLD = 20
LINE_THRESHOLD = 200
TEXT_THRESHOLD = 50


class App(tk.Frame):
    def __init__(self, window=None,
                 function_x=lambda t: 70 * math.pow(math.cos(t), 3) + math.log(t) - math.cos(t / 3),
                 function_y=lambda t: 70 * math.pow(math.sin(t), 3) + math.log(t) - math.sin(t / 3)):
        window.title(WINDOW_TITLE)
        window.geometry(WINDOW_GEOMETRY)
        super().__init__(window)
        self.master = window
        self.canvas = tk.Canvas(self.master, width=WINDOW_LENGTH, height=WINDOW_WIDTH)
        self.canvas.pack()
        self.pack()
        self.function_x = function_x
        self.function_y = function_y
        self.draw()

    def draw(self):
        x_coords, y_coords = self.get_data(0.1, 500, 0.1)
        self.create_axis()
        for i in range(len(x_coords)):
            self.canvas.create_rectangle((ZERO_X + x_coords[i], ZERO_Y - y_coords[i])*2)

    def create_axis(self):
        self.canvas.create_line(ZERO_X, ZERO_Y + LINE_THRESHOLD, ZERO_X, ZERO_Y - LINE_LENGTH)
        self.canvas.create_line(ZERO_X - LINE_THRESHOLD, ZERO_Y, ZERO_X + LINE_LENGTH, ZERO_Y)
        self.canvas.create_polygon(ZERO_X - ARROW_THRESHOLD, ZERO_Y - LINE_LENGTH,
                                   ZERO_X, ZERO_Y - LINE_LENGTH - ARROW_THRESHOLD,
                                   ZERO_X + ARROW_THRESHOLD, ZERO_Y - LINE_LENGTH)
        self.canvas.create_polygon(ZERO_X + LINE_LENGTH, ZERO_Y - ARROW_THRESHOLD,
                                   ZERO_X + LINE_LENGTH + ARROW_THRESHOLD, ZERO_Y,
                                   ZERO_X + LINE_LENGTH, ZERO_Y + ARROW_THRESHOLD)

        ordinate = tk.Label(self.master, text="f(x)")
        abcyss = tk.Label(self.master, text="x")
        ordinate.place(x=ZERO_X - TEXT_THRESHOLD, y=ZERO_Y - LINE_LENGTH)
        abcyss.place(x=ZERO_X + LINE_LENGTH, y=ZERO_Y - TEXT_THRESHOLD)

    def get_data(self, left, right, step):
        x = []
        y = []
        coordinate = left
        while coordinate < right:
            x.append(self.function_x(coordinate))
            y.append(self.function_y(coordinate))
            coordinate += step
        return x, y


if __name__ == '__main__':
    window = tk.Tk()
    app = App(window=window)
    app.mainloop()
