import torch
from PIL import Image
from PIL import ImageDraw
import PIL
from tkinter import *
import os, sys
sys.path.append(os.path.abspath(""))
from custom_neural_network import NeuralNetwork, NNTest, get_test_input_from_pil


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill='white', width=10)
    draw.line([x1, y1, x2, y2], fill='white', width=10)


def clear():
    draw.rectangle((0, 0, width, height), width=0, fill='black')
    canvas.delete('all')


def save():
    filename = "Custom test inputs/user_drawing.png"
    img.save(filename)
    test_input_nn = get_test_input_from_pil(img)
    print(f"Neural network classification for drawing: {nn_test.classify(test_input_nn)}")
    clear()


device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load('model_precise.pt'))
model.eval()
nn_test = NNTest(model)

width = 200
height = 200
center = height//2
master = Tk()
canvas = Canvas(master, width=width, height=height, bg='white')
canvas.pack()
img = PIL.Image.new("1", (width, height))
draw = ImageDraw.Draw(img)
canvas.pack(expand=YES, fill=BOTH)
canvas.bind("<B1-Motion>", paint)

# add a button to save the image
button = Button(text="Get result", command=save)
button.pack()

master.mainloop()
