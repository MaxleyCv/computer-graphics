import tkinter as tk


WINDOW_TITLE = "Lab #1"
WINDOW_WIDTH = 800
WINDOW_LENGTH = 800
WINDOW_GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_LENGTH}"

# Drawing constants
CIRCLE_RADIUS = 150

A = 160
a = 40


class App(tk.Frame):
    def __init__(self, window=None):
        window.title("Lab #1")
        window.geometry(WINDOW_GEOMETRY)
        super().__init__(window)
        self.master = window
        self.canvas = tk.Canvas(self.master, width=WINDOW_LENGTH, height=WINDOW_WIDTH)
        self.canvas.pack()
        self.pack()
        self.points = [WINDOW_WIDTH // 2, WINDOW_LENGTH // 2 - A // 2 - a,
                       WINDOW_WIDTH // 2 + a, WINDOW_LENGTH // 2 - A // 2 - a,

                       WINDOW_WIDTH // 2 + a, WINDOW_LENGTH // 2 - A // 2,
                      WINDOW_WIDTH // 2, WINDOW_LENGTH // 2 - A // 2]
        self.create_widgets()

    def create_widgets(self):
        self.create_sqare(WINDOW_WIDTH // 2, WINDOW_LENGTH // 2)
        self.create_small()

    def create_sqare(self, center_x, center_y):
        self.rectangle = self.canvas.create_rectangle(
            center_x - A // 2,
            center_y - A // 2,
            center_x + A // 2,
            center_y + A // 2,
            fill=None,
        )

    def create_small(self):
        self.canvas.create_polygon(*self.points, fill="black")


    def movement(self):


if __name__ == '__main__':
    window = tk.Tk()
    app = App(window=window)
    app.mainloop()
