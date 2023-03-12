from sketchpy import canvas
from turtle import Screen
s=Screen()
s.bgcolor("Black")

ab=canvas.sketch_from_svg("shivji.svg",scale=45)
ab.draw()
