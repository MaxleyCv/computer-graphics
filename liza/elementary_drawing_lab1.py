import tkinter as tk


WINDOW_TITLE = "Lab #1"
WINDOW_WIDTH = 800
WINDOW_LENGTH = 800
WINDOW_GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_LENGTH}"

# Drawing constants
CIRCLE_RADIUS = 150


class App(tk.Frame):
    def __init__(self, window=None):
        window.title("Lab #1")
        window.geometry(WINDOW_GEOMETRY)
        super().__init__(window)
        self.master = window
        self.canvas = tk.Canvas(self.master, width=WINDOW_LENGTH, height=WINDOW_WIDTH)
        self.canvas.pack()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_transistor(WINDOW_WIDTH // 2, WINDOW_LENGTH // 2)
        self.sign_transistor(WINDOW_WIDTH // 2, WINDOW_LENGTH // 2)

    def create_transistor(self, center_x, center_y):
        self.canvas.create_oval(center_x - CIRCLE_RADIUS, center_y - CIRCLE_RADIUS,
                                center_x + CIRCLE_RADIUS, center_y + CIRCLE_RADIUS)
        self.canvas.create_line(center_x - 1.5 * CIRCLE_RADIUS, center_y, center_x - 0.5 * CIRCLE_RADIUS, center_y)
        self.canvas.create_line(center_x - 0.5 * CIRCLE_RADIUS, center_y + 0.5 * CIRCLE_RADIUS,
                                center_x - 0.5 * CIRCLE_RADIUS, center_y - 0.5 * CIRCLE_RADIUS)

        self.canvas.create_line(center_x, center_y - 0.75 * CIRCLE_RADIUS,
                                center_x, center_y - 1.5 * CIRCLE_RADIUS)
        self.canvas.create_line(center_x, center_y + 0.75 * CIRCLE_RADIUS,
                                center_x, center_y + 1.5 * CIRCLE_RADIUS)

        self.canvas.create_line(center_x - 0.5 * CIRCLE_RADIUS, center_y - 0.25 * CIRCLE_RADIUS,
                                center_x, center_y - 0.75 * CIRCLE_RADIUS)
        self.canvas.create_line(center_x - 0.5 * CIRCLE_RADIUS, center_y + 0.25 * CIRCLE_RADIUS,
                                center_x, center_y + 0.75 * CIRCLE_RADIUS)

        self.create_arrow(center_x - 0.25 * CIRCLE_RADIUS, center_y - 0.5 * CIRCLE_RADIUS, 0.2 * CIRCLE_RADIUS)

    def create_arrow(self, center_x, center_y, height):
        self.canvas.create_polygon(center_x + height, center_y, center_x, center_y, center_x, center_y - height)

    def sign_transistor(self, center_x, center_y):
        collector = tk.Label(self.master, text="Collector", fg="black")
        collector.place(x=center_x + 0.1 * CIRCLE_RADIUS, y=center_y - 1.4 * CIRCLE_RADIUS)

        base = tk.Label(self.master, text="Base", fg="black")
        base.place(x=center_x - 1.5 * CIRCLE_RADIUS, y=center_y - 0.3 * CIRCLE_RADIUS)

        emiter = tk.Label(self.master, text="Emiter", fg="black")
        emiter.place(x=center_x + 0.1 * CIRCLE_RADIUS, y=center_y + 1.2 * CIRCLE_RADIUS)


if __name__ == '__main__':
    window = tk.Tk()
    app = App(window=window)
    app.mainloop()
