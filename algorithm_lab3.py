import tkinter as tk


WINDOW_TITLE = "Lab #1"
WINDOW_WIDTH = 800
WINDOW_LENGTH = 800
WINDOW_GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_LENGTH}"

# Drawing constants
CIRCLE_RADIUS = 100
LIGHT_HEIGHT = 700
LIGHT_WIDTH = 300
LAMP_THRESHOLD = 220


class App(tk.Frame):
    def __init__(self, window=None):
        window.title("Lab #1")
        window.geometry(WINDOW_GEOMETRY)
        super().__init__(window)
        self.master = window
        self.canvas = tk.Canvas(self.master, width=WINDOW_LENGTH, height=WINDOW_WIDTH)
        self.canvas.pack()
        self.pack()
#        button = self.init_button()
#        button.place(self.canvas, x=0, y=0)
        self.create_widgets()
    #
    #
    # def init_button(self):
    #     return tk.Button(function=self.create_widgets())

    def create_widgets(self):
        self.canvas.create_rectangle(WINDOW_WIDTH // 2 - LIGHT_WIDTH // 2, WINDOW_LENGTH // 2 - LIGHT_HEIGHT // 2,
                                     WINDOW_WIDTH // 2 + LIGHT_WIDTH // 2, WINDOW_LENGTH // 2 + LIGHT_HEIGHT // 2,
                                     fill="grey")
        fills = ["red", "yellow", "green"]
        for i in range(3):
            self.create_lamp(WINDOW_LENGTH // 2, WINDOW_WIDTH // 2 + (i - 1) * LAMP_THRESHOLD, fill=fills[i])

        # self.flood_fill([400, 400], "yellow")
        # self.flood_fill([400, 400 - LAMP_THRESHOLD], "red")
        # self.flood_fill([400, 400 + LAMP_THRESHOLD], "green")

        # print(self.canvas.create_bitmap())

    def create_lamp(self, center_x, center_y, fill):
        self.canvas.create_oval(center_x - CIRCLE_RADIUS, center_y - CIRCLE_RADIUS,
                                center_x + CIRCLE_RADIUS, center_y + CIRCLE_RADIUS, fill=fill)

    def flood_fill(self, start_point, color):
        x = start_point[0]
        y = start_point[1]
        if not self.inside(x, y):
            return
        if self.get_color(x, y):
            return
        try:
            self.flood_fill([x + 1, y + 1], color)
            self.flood_fill([x - 1, y - 1], color)
            self.flood_fill([x, y + 1], color)
            self.flood_fill([x + 1, y], color)
        except RecursionError:
            return

    def inside(self, x, y):
        return 0 <= x <= WINDOW_WIDTH and 0 <= y <= WINDOW_LENGTH

    def get_color(self, x, y):
        overlap = self.canvas.find_overlapping(x, y)


        if len(overlap):
            color = self.canvas.itemcget(overlap[-1], "fill")
            color = color.upper()
            return color

        return 0


if __name__ == '__main__':
    window = tk.Tk()
    app = App(window=window)
    app.mainloop()
