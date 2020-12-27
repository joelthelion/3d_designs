#!/usr/bin/env python3
""" Draw a chessboard that can be used for laser cutting with rdworks """

from pyx import canvas, path, color

if __name__ == '__main__':
    c = canvas.canvas()
    for i in range(8):
        for j in range(8):
            col = color.rgb.blue if (i+j)%2 == 0 else color.rgb.green
            c.stroke(path.rect(i,j,1,1), [col])
    c.writeSVGfile("chessboard.svg")
