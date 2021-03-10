from tkinter import Tk, Button, Label, DoubleVar, Entry

#App User Interface
appWindow = Tk()
appWindow.title("Meter to Feet Conversion App")
appWindow.configure(background = "grey20")
appWindow.geometry("320x240")
appWindow.resizable(width = False, height = False)

def convert():
    value = float(mt_entry.get())
    feet = value * 3.28084
    ft_value.set("%.4f" %feet)

def clear():
    mt_value.set("")
    ft_value.set("")

mt_lbl = Label(appWindow, text="Meter", bg= "blueviolet", fg="white", width = 14)
mt_lbl.grid(column = 0, row = 0, padx = 30, pady = 30)

mt_value = DoubleVar()
mt_entry = Entry(appWindow, textvariable = mt_value, width = 14)
mt_entry.grid(column = 1, row = 0)
mt_entry.delete(0,'end')

ft_lbl = Label(appWindow, text="Feet", bg= "blueviolet", fg="white", width = 14)
ft_lbl.grid(column = 0, row = 1, padx = 30, pady = 15)

ft_value = DoubleVar()
ft_entry = Entry(appWindow, textvariable = ft_value, width = 14)
ft_entry.grid(column = 1, row = 1)
ft_entry.delete(0,'end')

convert_button = Button(appWindow, text = "Convert", bg = "royalblue2", fg = "white", width = 14, command = convert)
convert_button.grid(column = 0, row = 3, padx = 30, pady = 30 )

clear_button = Button(appWindow, text = "Clear", bg = "red3", fg = "white", width = 14, command =clear)
clear_button.grid(column = 1, row = 3, padx = 15)

appWindow.mainloop()