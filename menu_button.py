from tkinter import *



root = Tk()
root.geometry("400x400")

mb = Menubutton(root, text="This is a menu")
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1", command=lambda: print("This is option 1"))
mb.menu.add_command(label="Option 2", command=lambda: print("This is option 2"))
mb.menu.add_comment(label="Option 3", command=lambda: print("This is option 3"))
mb.menu.add_comment(label="Option 4", command=lambda: print("This is Option 4"))




mb.pack()


root.mainloop()