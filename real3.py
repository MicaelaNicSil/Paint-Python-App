from textwrap import fill
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import Canvas, Tk, Frame, Button, messagebox, filedialog, Scale, HORIZONTAL, ALL
from turtle import bgcolor

import PIL.ImageGrab as ImageGrab
from tkinter import ttk, colorchooser

class Paint_Program(object):
    line_x = 0
    line_y = 0
    pen_size = 5.0
    pen_color = 'black'

    def __init__(self):
        self.root = Tk()
       
        self.color_bg_frame= "pink"
        self.color_bg = 'white'

        self.canvas = Canvas(self.root, bg= self.color_bg, width=900, height=600)
        self.canvas.grid(row=1, column= 0, columnspan=7)
            
        self.pen_bt = Button(self.root, text='pen', command=self.use_pen)
        self.pen_bt.grid(row=0, column=0)

        self.color_bt = Button(self.root, text='color', command=self.choose_color)
        self.color_bt.grid(row=0, column=1)

        self.eraser_bt = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_bt.grid(row=0, column=2)
    
        self.size_bt = Scale(self.root,  from_=1, to=100, orient=HORIZONTAL)
        self.size_bt.set(1)
        self.size_bt.grid(row=0, column=4, ipadx=30)

        self.bt_save = Button(self.root, text='save', command=self.save_drawing)
        self.bt_save.grid(row=0, column=5)

        self.bt_clear = Button(self.root, text='clear', command=self.clear)
        self.bt_clear.grid(row=0, column=6)
        
        
        
        self.canvas.bind('<Button-1>', self.line_xy)#drwaing the line 
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
             

        self.Dwidgets()
        self.root.mainloop()

    def Dwidgets(self):
        self.old_x = None
        self.old_y = None

        self.line_width = self.size_bt.get()
        
        self.color = self.pen_color

        self.eraser_on = False

        self.active_button = self.pen_bt
        

        self.frame_controls = Frame(self.root, height=100)
        self.frame_controls.grid(column = 3, row=0, sticky = "ew", )
        self.frame_controls.columnconfigure(0, minsize=200, weight=1)
        Label(self.frame_controls, text='Pen Width:',font=('arial 15')).grid(row=3,column=0)

        self.use_pen()   
        
    def paint(self, event):
        self.line_width = self.size_bt.get()
        paint_color = self.color_bg if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.line_width, fill=paint_color,
                                    capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def use_pen(self):
        self.activate_button(self.pen_bt)


    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]



    def use_eraser(self):
        self.activate_button(self.eraser_bt, eraser_mode=True)


    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode   


    def line_xy(self, event):
        self.line_x
        self.line_y
    
        self.line_x = event.x
        self.line_y = event.y
    
    def line(self, event):
        self.line_x, self.line_y, 
        self.canvas.create_line((self.line_x, self.line_y, event.x, event.y), fill=self.pen_color, width = self.line_width.get())
        self.line_x = event.x
        self.line_y = event.y

    def slider(self):
        self.slider = ttk.Scale(self.frame_controls,from_= 5, to = 100,command=self.changeW,orient=HORIZONTAL)
        self.slider.set(self.penwidth)

    def reset(self, event):
        self.old_x, self.old_y = None, None 

    def clear(self):
        self.canvas.delete(ALL)

    


    def save_drawing(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".png")
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = (self.root.winfo_rooty() + self.canvas.winfo_y())
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
            messagebox.showinfo("Save drawing", "Image saved in:" + str(filename))
        except:
            messagebox.showerror("Save drawing", "Image not saved\n Error")
   


if __name__ == '__main__':
    Paint_Program()




