import os.path
import sys
from tkinter import BOTH, Button, Canvas, Tk, YES

import PIL
from PIL import Image, ImageDraw

parent_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if parent_dir_path not in sys.path:
    sys.path.insert(0, parent_dir_path)

from ml_digits_recognition.neural_network import get_test_input_from_pil, load_nn_test

dir_path = os.path.dirname(os.path.realpath(__file__))


def run():
    nn_test = load_nn_test()

    width = 200
    height = 200
    center = height // 2
    master = Tk()
    canvas = Canvas(master, width=width, height=height, bg='white')
    canvas.pack()
    img = PIL.Image.new("1", (width, height))
    draw = ImageDraw.Draw(img)

    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(x1, y1, x2, y2, fill='white', width=10)
        draw.line([x1, y1, x2, y2], fill='white', width=10)

    def clear():
        draw.rectangle((0, 0, width, height), width=0, fill='black')
        canvas.delete('all')

    def save():
        save_dir = 'Custom test inputs'
        if os.path.exists(save_dir):
            file_path = os.path.join(dir_path, save_dir, "user_drawing.png")
            img.save(file_path)
        test_input_nn = get_test_input_from_pil(img)
        print(f"Neural network classification for drawing: {nn_test.classify(test_input_nn)}")
        clear()

    canvas.pack(expand=YES, fill=BOTH)
    canvas.bind("<B1-Motion>", paint)

    # add a button to save the image
    button = Button(text="Get result", command=save)
    button.pack()

    master.mainloop()


if __name__ == '__main__':
    run()
