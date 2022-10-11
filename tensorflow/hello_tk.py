#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
A simple script to check tkinter install successfully
'''

from tkinter import Tk
from tkinter import Label

def main():
    '''main function'''
    root = Tk()
    window = Label(root, text="Hello, world!")
    window.pack()
    root.mainloop()

if __name__ == '__main__':
    main()

#EOF
