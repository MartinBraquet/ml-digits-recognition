import os.path
from tkinter import BOTH, Button, Canvas, Tk, YES

import PIL
import torch
from PIL import Image, ImageDraw
from ml_digits_recognition.neural_network import NNTest, NeuralNetwork, get_test_input_from_pil

dir_path = os.path.dirname(os.path.realpath(__file__))

def run():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = NeuralNetwork().to(device)
    path = os.path.join(dir_path, 'model_precise.pt')
    model.load_state_dict(torch.load(path))
    model.eval()
    nn_test = NNTest(model)

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